from django.urls import path

from PizzaProject.profiles.views import Orders, ProfileDetails, RepeatOrderAPIView

urlpatterns = [
    path('details/<int:pk>/', ProfileDetails.as_view(), name='profile_details'),
    path('orders/<int:pk>/', Orders.as_view(), name='orders'),
    path('api/repeat-order/', RepeatOrderAPIView.as_view(), name='repeat_order_api')

]
