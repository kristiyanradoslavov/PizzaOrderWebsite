from django.urls import reverse_lazy
from django.views import generic as generic_views
from django.contrib.auth import mixins as auth_mixins, get_user_model
from rest_framework.response import Response
from rest_framework import generics as rest_generic_views, status

from PizzaProject.order.models import OrderHistory, OrderItem
from PizzaProject.order.serializers import CreateItemSerializer
from PizzaProject.profiles.forms import ProfileForm
from PizzaProject.profiles.models import Profile

UserModel = get_user_model()


class ProfileDetails(generic_views.UpdateView):
    template_name = 'form_templates/profile-details.html'
    form_class = ProfileForm
    model = Profile
    success_url = reverse_lazy('home_page')

    def get_form_kwargs(self):
        kwargs = super().get_form_kwargs()
        kwargs['initial'] = {
            'email': self.request.user.email
        }

        return kwargs

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        image_url = self.request.user.profile.image
        context['image_url'] = image_url

        return context


class Orders(auth_mixins.LoginRequiredMixin, generic_views.ListView):
    template_name = 'form_templates/order-history.html'
    model = OrderHistory

    def get_queryset(self):
        return OrderHistory.objects.filter(user_id=self.request.user.id).order_by('-date_created')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        order_history_list = self.get_queryset()

        grouped_orders = {}

        for order in order_history_list:
            if order.specific_order_id not in grouped_orders:
                grouped_orders[order.specific_order_id] = [order]
            else:
                grouped_orders[order.specific_order_id].append(order)

        page_number = int(self.request.GET.get('page', 1))
        items_per_page = 5  # Change this as needed
        total_pages = (len(grouped_orders) + items_per_page - 1) // items_per_page
        start_index = (page_number - 1) * items_per_page
        end_index = start_index + items_per_page
        current_page_orders = list(grouped_orders.values())[start_index:end_index]

        context['grouped_orders'] = current_page_orders
        context['page_number'] = int(page_number)
        context['total_pages'] = total_pages

        return context


class RepeatOrderAPIView(rest_generic_views.CreateAPIView):
    serializer_class = CreateItemSerializer

    def create(self, request, *args, **kwargs):
        specific_order_id = request.data.get('specific_order_id')

        try:
            order_history = OrderHistory.objects.filter(specific_order_id=specific_order_id).all()
        except OrderHistory.DoesNotExist:
            return Response({'detail': f"Order with specific_order_id {specific_order_id} not found."},
                            status=status.HTTP_404_NOT_FOUND)

        current_order_items = OrderItem.objects.filter(user_id=self.request.user.id).all()
        existing_items_in_cart = [p.price_id for p in current_order_items]

        order_items = []
        for order in order_history:
            if order.price_id not in existing_items_in_cart:
                order_item = OrderItem(
                    product_name=order.product_name,
                    product_id=order.product_id,
                    quantity=order.quantity,
                    size=order.size,
                    single_price=order.single_price,
                    image=order.image,
                    user=order.user,
                    price_id=order.price_id
                )
                order_items.append(order_item)

        OrderItem.objects.bulk_create(order_items)

        return Response({'detail': f"Order items for specific_order_id {specific_order_id} created successfully."},
                        status=status.HTTP_201_CREATED)
