from django.urls import path
from PizzaProject.user_authentication.views import RegisterUser, LoginUser, LogoutUser, DeleteRequest, ChangePassword, \
    DeleteProfileConfirm

urlpatterns = [
    path('register/', RegisterUser.as_view(), name='register_user'),
    path('login/', LoginUser.as_view(), name='login_user'),
    path('logout/', LogoutUser.as_view(), name='logout_user'),
    path('delete/<int:pk>/', DeleteRequest.as_view(), name='delete_profile'),
    path('delete/confirm/<int:pk>/', DeleteProfileConfirm.as_view(), name='delete_confirm'),
    path('pass/<int:pk>/', ChangePassword.as_view(), name='change_password'),
]
