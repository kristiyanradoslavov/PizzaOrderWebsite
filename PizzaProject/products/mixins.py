# from django.shortcuts import redirect
# from django.views import generic as generic_views
#
# from PizzaProject.order.models import OrderItem
#
#
# class ProductFormValidationMixin:
#
#
#     def form_valid(self, form):
#         result = super().form_valid(form)
#
#         previous_url = self.request.session['previous_url']
#         current_product = self.get_context_data()['product']
#
#         ordered_quantity = form.cleaned_data.get('quantity')
#         ordered_quantity = form.cleaned_data.get('quantity')
#
#         current_order = OrderItem.objects.create(
#             product_type=current_product.__class__.__name__,
#             product_id=current_product.pk,
#             # quantity=
#         )
#
#         if previous_url:
#             return redirect(previous_url)
#
#         return result
