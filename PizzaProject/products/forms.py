from django import forms

from PizzaProject.products.models import Pizza


class PizzaDetailsForm(forms.Form):
    SIZE_CHOICES = (
        ('Small', 'Small'),
        ('Medium', 'Medium'),
        ('Large', 'Large'),
        ('Extra Large', 'Extra Large'),
    )

    size = forms.ChoiceField(choices=SIZE_CHOICES, widget=forms.RadioSelect())
    quantity = forms.IntegerField(min_value=1, initial=1)
