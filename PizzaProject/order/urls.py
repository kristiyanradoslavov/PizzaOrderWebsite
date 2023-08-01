from django.urls import path

from PizzaProject.order.views import CreateOrder, SuccessView, CancelView, stripe_webhook

urlpatterns = [
    path('create/', CreateOrder.as_view(), name='create_order'),
    path("success/", SuccessView.as_view(), name="successful_payment"),
    path("cancel/", CancelView.as_view(), name="canceled_payment"),
    path('webhook/stripe/', stripe_webhook, name='stripe_webhook')
]
