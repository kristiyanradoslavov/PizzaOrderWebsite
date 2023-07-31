import stripe
from django.contrib.auth import get_user_model
from django.shortcuts import redirect
from django.views import generic as generic_views

from PizzaProject import settings
from PizzaProject.order.forms import CreateOrderForm
from PizzaProject.order.models import OrderItem
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
        payment_type = form.cleaned_data['sizes']
        if payment_type == "Cash":
            return redirect("home_page")

        all_ordered_items = OrderItem.objects.filter(user_id=self.request.user).all()
        item_information = []
        for current_product in all_ordered_items:
            item_information.append({
                'price': current_product.price_id,
                'quantity': current_product.quantity,
            })

        # price = Price.objects.get(id=self.kwargs["pk"])
        if settings.DEBUG:
            domain = "http://127.0.0.1:8000"
        checkout_session = stripe.checkout.Session.create(
            payment_method_types=['card'],
            line_items=item_information,
            mode='payment',
            success_url=domain + '/success/',
            cancel_url=domain + '/cancel/',
        )
        return redirect(checkout_session.url)



#
# class CreateCheckoutSessionView(generic_views.View):
#     def post(self, request, *args, **kwargs):
#         all_ordered_items = OrderItem.objects.filter(user_id=self.request.user).all()
#         item_information = []
#         for current_product in all_ordered_items:
#             item_information.append({
#                 'price': current_product.price_id,
#                 'quantity': current_product.quantity,
#             })
#
#         # price = Price.objects.get(id=self.kwargs["pk"])
#         if settings.DEBUG:
#             domain = "http://127.0.0.1:8000"
#         checkout_session = stripe.checkout.Session.create(
#             payment_method_types=['card'],
#             line_items=item_information,
#             mode='payment',
#             success_url=domain + '/success/',
#             cancel_url=domain + '/cancel/',
#         )
#         return redirect(checkout_session.url)


class SuccessView(generic_views.TemplateView):
    template_name = 'order/success.html'


class CancelView(generic_views.TemplateView):
    template_name = 'order/cancel.html'
