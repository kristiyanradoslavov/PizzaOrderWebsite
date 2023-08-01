from django import forms

from PizzaProject.profiles.models import Profile


class CreateOrderForm(forms.ModelForm):
    PAYMENT_CHOICES = (
        ('Cash', 'Cash'),
        ('Credit Card', 'Credit Card')
    )

    payment_options = forms.ChoiceField(choices=PAYMENT_CHOICES, widget=forms.RadioSelect())
    product_items = forms.BooleanField(
        error_messages={
            'required': 'Add products in the cart before ordering.'
        }
    )

    class Meta:
        model = Profile
        fields = ('first_name', 'last_name', 'phone_number', 'city', 'address')
