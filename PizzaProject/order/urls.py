from django.urls import path

from PizzaProject.order.views import CreateOrder

urlpatterns = [
    path('create/', CreateOrder.as_view(), name='create_order'),
]
