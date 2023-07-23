from django.contrib import admin
from django.urls import path, include
from PizzaProject.products.views import PizzaMenu, SaladMenu, DesertMenu, DrinksMenu, HomePage, PizzaDetails, \
    SaladDetails, DesertDetails, DrinksDetails

urlpatterns = [
    path('', HomePage.as_view(), name='home_page'),
    path('pizza/', include([
        path('', PizzaMenu.as_view(), name='pizza_menu'),
        path('details/<slug:slug>/', PizzaDetails.as_view(), name='pizza_details'),
    ])),
    path('salad/', include([
        path('', SaladMenu.as_view(), name='salad_menu'),
        path('details/<slug:slug>/', SaladDetails.as_view(), name='salad_details'),
    ])),
    path('dessert/', include([
        path('', DesertMenu.as_view(), name='dessert_menu'),
        path('details/<slug:slug>/', DesertDetails.as_view(), name='desert_details'),
    ])),
    path('drink/', include([
        path('', DrinksMenu.as_view(), name='drinks_menu'),
        path('details/<slug:slug>/', DrinksDetails.as_view(), name='drink_details'),
    ])),
]
