from django.utils.translation import gettext_lazy as _

from django.contrib.auth import forms as auth_forms, get_user_model
from django.contrib.auth.forms import SetPasswordForm

from PizzaProject import settings

UserModel = get_user_model()


class RegisterForm(auth_forms.UserCreationForm):
    class Meta(auth_forms.UserCreationForm):
        model = UserModel
        fields = ("email", 'password1', 'password2')


class ChangePasswordForm(auth_forms.PasswordChangeForm):
    error_messages = {
        **SetPasswordForm.error_messages,
        "password_incorrect": _(
            "The entered password didn`t match. Please try again."
        ),
    }
