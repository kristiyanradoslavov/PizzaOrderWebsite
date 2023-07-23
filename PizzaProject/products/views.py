from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views import generic as generic_views

from PizzaProject.order.models import OrderItem
from PizzaProject.products.forms import PizzaDetailsForm
from PizzaProject.products.models import Pizza, Salad, Desert, Drink


class HomePage(generic_views.TemplateView):
    template_name = 'home_page/home-page.html'


class PizzaMenu(generic_views.ListView):
    template_name = 'products/pizza-menu.html'
    model = Pizza


class PizzaDetails(generic_views.FormView):
    template_name = 'products/product_details/pizza-details.html'
    form_class = PizzaDetailsForm
    success_url = reverse_lazy('create_order')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        product_slug = self.kwargs.get('slug')
        pizza = Pizza.objects.filter(slug=product_slug).get()
        context['product'] = pizza

        return context

    def form_valid(self, form):
        result = super().form_valid(form)

        previous_url = self.request.session['previous_url']
        current_product = self.get_context_data()['product']

        ordered_quantity = form.cleaned_data.get('quantity')
        ordered_quantity = form.cleaned_data.get('quantity')

        current_order = OrderItem.objects.create(
            product_type=current_product.__class__.__name__,
            product_id=current_product.pk,
            # quantity=
        )

        if previous_url:
            return redirect(previous_url)

        return result

    def get(self, request, *args, **kwargs):
        result = super().get(request, *args, **kwargs)
        self.request.session['previous_url'] = self.request.META.get('HTTP_REFERER')

        return result

    # def get_success_url(self):
    #     return self.request.POST.get('previous', self.success_url)


class SaladMenu(generic_views.ListView):
    template_name = 'products/salad-menu.html'
    model = Salad


class SaladDetails(generic_views.DetailView):
    template_name = 'products/product_details/salad-details.html'
    model = Salad


class DesertMenu(generic_views.ListView):
    template_name = 'products/desert-menu.html'
    model = Desert


class DesertDetails(generic_views.DetailView):
    template_name = 'products/product_details/desert-details.html'
    model = Desert


class DrinksMenu(generic_views.ListView):
    template_name = 'products/drinks-menu.html'
    model = Drink


class DrinksDetails(generic_views.DetailView):
    template_name = 'products/product_details/drinks-details.html'
    model = Drink
