import stripe
from django.http import HttpResponse
from django.shortcuts import redirect
from django.urls import reverse_lazy
from django.views import generic as generic_views
from django.views.decorators.csrf import csrf_exempt
from rest_framework.response import Response
from rest_framework import generics as rest_generic_views, status

from PizzaProject import settings
from PizzaProject.order.forms import CreateOrderForm
from PizzaProject.order.models import OrderItem
from PizzaProject.order.serializers import OrderItemSerializer, DeleteItemSerializer, GetItemsSerializer
from PizzaProject.order.util_functions import clear_order_items, create_order_history_item
from PizzaProject.profiles.forms import ProfileForm

stripe.api_key = settings.STRIPE_SECRET_KEY


class CreateOrder(generic_views.FormView):
    template_name = 'order/shopping-cart.html'
    form_class = CreateOrderForm

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        all_products = {}

        all_ordered_items = OrderItem.objects.filter(user_id=self.request.user)
        total_price = 0

        for product in all_ordered_items:
            current_product_price = product.quantity * product.single_price
            all_products[product] = current_product_price
            total_price += current_product_price

        context['all_products_dict'] = all_products
        context['total_price'] = total_price

        current_profile = self.request.user.profile
        current_profile_form = ProfileForm(instance=current_profile)

        context['profile_form'] = current_profile_form
        context['current_user'] = current_profile

        return context

    def form_valid(self, form):
        payment_type = form.cleaned_data['payment_options']
        all_filled_data = form.cleaned_data

        if payment_type == "Cash":
            create_order_history_item(self.request.user.id)
            clear_order_items(self.request.user.id)
            return redirect('successful_payment')

        all_ordered_items = OrderItem.objects.filter(user_id=self.request.user).all()
        item_information = []
        for current_product in all_ordered_items:
            item_information.append({
                'price': current_product.price_id,
                'quantity': current_product.quantity,
            })

        if not settings.DEBUG:
            domain = 'http://localhost:8000'
        else:
            domain = f'http://{settings.ALLOWED_HOSTS[0]}'

        checkout_session = stripe.checkout.Session.create(
            payment_method_types=['card'],
            line_items=item_information,
            mode='payment',
            success_url=domain + '/order/success/',
            cancel_url=domain + '/order/cancel/',
            metadata={
                **all_filled_data,
                'customer_id': self.request.user.id,
            }
        )
        return redirect(checkout_session.url)


class SuccessView(generic_views.TemplateView):
    template_name = 'order/success.html'


class CancelView(generic_views.TemplateView):
    template_name = 'order/cancel.html'


@csrf_exempt
def stripe_webhook(request):
    payload = request.body
    sig_header = request.META['HTTP_STRIPE_SIGNATURE']
    event = None

    try:
        event = stripe.Webhook.construct_event(
            payload, sig_header, settings.STRIPE_WEBHOOK_SECRET
        )
    except ValueError as e:
        # Invalid payload
        return HttpResponse(status=400)
    except stripe.error.SignatureVerificationError as e:
        # Invalid signature
        return HttpResponse(status=400)

    if event['type'] == 'checkout.session.completed':
        # Retrieve the session. If you require line items in the response, you may include them by expanding line_items.
        session = stripe.checkout.Session.retrieve(
            event['data']['object']['id'],
            expand=['line_items'],
        )

        customer_id = session['metadata']['customer_id']

        line_items = session.line_items

        create_order_history_item(customer_id)
        clear_order_items(customer_id)

    return HttpResponse(status=200)


class UpdateCartItemAPIView(rest_generic_views.UpdateAPIView):
    queryset = OrderItem.objects.all()
    serializer_class = OrderItemSerializer

    def update(self, request, *args, **kwargs):
        instance = self.get_object()
        new_quantity = int(request.data.get('new_quantity'))

        instance.quantity = new_quantity
        instance.save()

        serializer = OrderItemSerializer(instance)
        return Response(serializer.data, status=status.HTTP_200_OK)


class DeleteCartItemAPIView(rest_generic_views.DestroyAPIView):
    queryset = OrderItem.objects.all()
    serializer_class = DeleteItemSerializer


class GetCartQuantityAPIView(rest_generic_views.ListAPIView):
    serializer_class = GetItemsSerializer

    def get_queryset(self):
        user_id = self.request.user.id

        try:
            cart = OrderItem.objects.filter(user_id=user_id).all()
            return cart

        except OrderItem.DoesNotExist:
            return OrderItem.objects.none()
