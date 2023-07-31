from django.urls import path

from PizzaProject.order.views import CreateOrder, SuccessView, CancelView

urlpatterns = [
    path('create/', CreateOrder.as_view(), name='create_order'),
    # path('chckout-session/', CreateCheckoutSessionView.as_view(), name='create_checkout_session'),
    path("success/", SuccessView.as_view(), name="successful_payment"),
    path("cancel/", CancelView.as_view(), name="canceled_payment"),
]
