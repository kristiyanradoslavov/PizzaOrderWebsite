from django.contrib.auth import get_user_model
from django.shortcuts import redirect
from django.contrib.auth.views import redirect_to_login

from PizzaProject.order.models import OrderItem


class ProductFormValidationMixin:
    product = None
    product_available_sizes = None

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        product_slug = self.kwargs.get('slug')
        product = self.product.filter(slug=product_slug).get()

        if self.product_available_sizes == "Small":
            sizes = {
                'Small': product.price_small,
                'Large': product.price_large,
            }
        elif self.product_available_sizes == "Large":
            sizes = {
                'Small': product.price_small,
                'Medium': product.price_medium,
                'Large': product.price_large,
                'extra_large': product.price_extra_large,
            }
        else:
            sizes = {
                'single_price': product.price,
            }

        context['product'] = product
        context['product_sizes'] = sizes

        return context

    def form_valid(self, form):
        result = super().form_valid(form)

        current_product = self.get_context_data()['product']
        all_sizes = self.get_context_data()['product_sizes']

        ordered_quantity = form.cleaned_data.get('quantity')
        ordered_size = form.cleaned_data.get('size')

        if ordered_size == "Small":
            stripe_price_id = current_product.stripe_small_price_id
        elif ordered_size == "Medium":
            stripe_price_id = current_product.stripe_medium_price_id
        elif ordered_size == "Large":
            stripe_price_id = current_product.stripe_large_price_id
        elif ordered_size == "Extra Large":
            stripe_price_id = current_product.stripe_extra_large_price_id
        else:
            stripe_price_id = current_product.stripe_single_price_id

        if current_product.__class__.__name__ != 'Drink':
            product_image = current_product.image
        else:
            if ordered_size == "Small":
                product_image = current_product.small_image
            else:
                product_image = current_product.large_image

        if "single_price" not in all_sizes.keys():
            size = 'extra_large' if ordered_size == 'Extra Large' else ordered_size
            current_price = all_sizes[size]
        else:
            current_price = current_product.price

        ordered_product = OrderItem.objects.filter(
            user_id=self.request.user,
            product_id=current_product.pk,
            size=ordered_size,
            product_name=current_product.name
        )

        if ordered_product:
            product = ordered_product.get()
            current_quantity = product.quantity
            new_quantity = current_quantity + ordered_quantity
            ordered_product.update(quantity=new_quantity)
        else:
            OrderItem.objects.create(
                product_name=current_product.name,
                product_id=current_product.pk,
                quantity=ordered_quantity,
                size=ordered_size,
                single_price=current_price,
                user=self.request.user,
                image=product_image,
                price_id=stripe_price_id
            )

        return result

    def dispatch(self, request, *args, **kwargs):
        if not request.user.is_authenticated and self.request.method == 'POST':
            return redirect_to_login(self.request.get_full_path(), login_url='/user/login/')
        return super().dispatch(request, *args, **kwargs)
