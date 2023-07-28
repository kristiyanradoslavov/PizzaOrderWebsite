from django.contrib.auth import get_user_model
from django.views import generic as generic_views

from PizzaProject.order.models import OrderItem
from PizzaProject.profiles.forms import ProfileForm


class CreateOrder(generic_views.TemplateView):
    template_name = 'order/shopping-cart.html'

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
