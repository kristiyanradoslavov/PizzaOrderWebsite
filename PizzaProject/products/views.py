from django.urls import reverse_lazy
from django.views import generic as generic_views
from django.contrib.auth import mixins as auth_mixins, get_user_model

from PizzaProject.products.forms import PizzaDetailsForm, SaladDetailsForm, DrinkDetailsForm, DesertDetailsForm
from PizzaProject.products.mixins import ProductFormValidationMixin
from PizzaProject.products.models import Pizza, Salad, Desert, Drink


class HomePage(generic_views.TemplateView):
    template_name = 'home_page/home-page.html'


class PizzaMenu(generic_views.ListView):
    template_name = 'products/pizza-menu.html'
    model = Pizza


class PizzaDetails(ProductFormValidationMixin, generic_views.FormView):
    template_name = 'products/product_details/pizza-details.html'
    form_class = PizzaDetailsForm
    success_url = reverse_lazy('create_order')
    product = Pizza.objects.all()
    product_available_sizes = 'Large'


class SaladMenu(generic_views.ListView):
    template_name = 'products/salad-menu.html'
    model = Salad


class SaladDetails(ProductFormValidationMixin, generic_views.FormView):
    template_name = 'products/product_details/salad-details.html'
    form_class = SaladDetailsForm
    success_url = reverse_lazy('create_order')
    product = Salad.objects.all()
    product_available_sizes = 'Small'


class DesertMenu(generic_views.ListView):
    template_name = 'products/desert-menu.html'
    model = Desert


class DesertDetails(ProductFormValidationMixin, generic_views.FormView):
    template_name = 'products/product_details/desert-details.html'
    form_class = DesertDetailsForm
    success_url = reverse_lazy('create_order')
    product = Desert.objects.all()


class DrinksMenu(generic_views.ListView):
    template_name = 'products/drinks-menu.html'
    model = Drink


class DrinksDetails(ProductFormValidationMixin, generic_views.FormView):
    template_name = 'products/product_details/drinks-details.html'
    form_class = DrinkDetailsForm
    success_url = reverse_lazy('create_order')
    product = Drink.objects.all()
    product_available_sizes = 'Small'
