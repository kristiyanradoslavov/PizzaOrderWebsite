from django import forms
from django.contrib.auth import get_user_model

from PizzaProject.profiles.models import Profile

UserModel = get_user_model()


class ProfileForm(forms.ModelForm):
    email = forms.EmailField(disabled=True)

    class Meta:
        model = Profile
        exclude = ('user',)

