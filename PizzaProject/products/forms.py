from django import forms


class BaseDetailsForm(forms.Form):
    quantity = forms.IntegerField(min_value=1, initial=1)

    def __init__(self, *args, **kwargs):
        size_choices = kwargs.pop('size_choices', None)
        super().__init__(*args, **kwargs)

        if size_choices:
            self.fields['size'] = forms.ChoiceField(choices=size_choices, widget=forms.RadioSelect())


class PizzaDetailsForm(BaseDetailsForm):
    SIZE_CHOICES = (
        ('Small', 'Small'),
        ('Medium', 'Medium'),
        ('Large', 'Large'),
        ('Extra Large', 'Extra Large'),
    )

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs, size_choices=self.SIZE_CHOICES)


class SaladDetailsForm(BaseDetailsForm):
    SIZE_CHOICES = (
        ('Small', 'Small'),
        ('Large', 'Large'),
    )

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs, size_choices=self.SIZE_CHOICES)


class DesertDetailsForm(BaseDetailsForm):
    pass


class DrinkDetailsForm(BaseDetailsForm):
    SIZE_CHOICES = (
        ('Small', 'Small'),
        ('Large', 'Large'),
    )

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs, size_choices=self.SIZE_CHOICES)