from django.urls import path

from PizzaProject.order.views import CreateOrder, SuccessView, CancelView, stripe_webhook, UpdateCartItemAPIView, \
    DeleteCartItemAPIView, GetCartQuantityAPIView

urlpatterns = [
    path('create/', CreateOrder.as_view(), name='create_order'),
    path("success/", SuccessView.as_view(), name="successful_payment"),
    path("cancel/", CancelView.as_view(), name="canceled_payment"),
    path('webhook/stripe/', stripe_webhook, name='stripe_webhook'),
    path('api/update-quantity/<int:pk>/', UpdateCartItemAPIView.as_view(), name='update_quantity_api'),
    path('api/delete-item/<int:pk>/', DeleteCartItemAPIView.as_view(), name='delete_cart_item'),
    path('api/get-all-items/', GetCartQuantityAPIView.as_view(), name='get_all_cart_items'),
]
