from django.contrib import admin

from PizzaProject.products.models import Pizza, Salad, Desert, Drink


class BaseProductAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'slug', ]
    search_fields = ['name', ]
    list_display_links = ['id', 'name']
    search_help_text = 'Search by Name of the product.'


@admin.register(Pizza)
class PizzaAdmin(BaseProductAdmin):
    fieldsets = (
        ('Product information', {
            'fields': ('name', 'description', 'image')
        }),
        ('Price Information', {
            'fields': ('price_small', 'price_medium', 'price_large', 'price_extra_large')
        }),
        ('Stripe prices', {
            'fields': (
                'stripe_small_price_id', 'stripe_medium_price_id', 'stripe_large_price_id',
                'stripe_extra_large_price_id'
            )
        })
    )


@admin.register(Salad)
class SaladAdmin(BaseProductAdmin):
    fieldsets = (
        ('Product information', {
            'fields': ('name', 'description', 'image')
        }),
        ('Price Information', {
            'fields': ('price_small', 'price_large')
        }),
        ('Stripe prices', {
            'fields': ('stripe_small_price_id', 'stripe_large_price_id')
        })
    )


@admin.register(Desert)
class DesertAdmin(BaseProductAdmin):
    fieldsets = (
        ('Product information', {
            'fields': ('name', 'description', 'image')
        }),
        ('Price Information', {
            'fields': ('price',)
        }),
        ('Stripe prices', {
            'fields': ('stripe_single_price_id',)
        })
    )


@admin.register(Drink)
class DrinkAdmin(BaseProductAdmin):
    fieldsets = (
        ('Product information', {
            'fields': ('name', 'description', 'small_image', 'large_image')
        }),
        ('Price Information', {
            'fields': ('price_small', 'price_large')
        }),
        ('Stripe prices', {
            'fields': ('stripe_small_price_id', 'stripe_large_price_id')
        })
    )
