from django import forms


class CreateOrderForm(forms.Form):
    PAYMENT_CHOICES = (
        ('Cash', 'Cash'),
        ('Credit Card', 'Credit Card')
    )

    sizes = forms.ChoiceField(choices=PAYMENT_CHOICES, widget=forms.RadioSelect())
