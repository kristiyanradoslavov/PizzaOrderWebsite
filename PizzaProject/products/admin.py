from django.contrib import admin

from PizzaProject.products.models import Pizza, Salad, Desert, Drink


@admin.register(Pizza)
class PizzaAdmin(admin.ModelAdmin):
    pass


@admin.register(Salad)
class SaladAdmin(admin.ModelAdmin):
    pass


@admin.register(Desert)
class SaladAdmin(admin.ModelAdmin):
    pass


@admin.register(Drink)
class SaladAdmin(admin.ModelAdmin):
    pass
