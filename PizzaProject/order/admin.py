from django.contrib import admin

from PizzaProject.order.models import OrderItem, OrderHistory


class OrderBaseAdmin(admin.ModelAdmin):
    search_help_text = 'Search by Name of the product or Size.'
    search_fields = ['product_name', 'size']
    list_display_links = ['id', 'product_name']
    fieldsets = (
        ('User Information', {
            'fields': ('user',)
        }),
        ('Product Information', {
            'fields': ('product_name', 'product_id', 'quantity', 'size', 'single_price', 'image', 'price_id')
        }),
    )


@admin.register(OrderItem)
class OrderItemAdmin(OrderBaseAdmin):
    list_display = ['id', 'product_name', 'size', 'quantity', 'single_price', 'user']
    list_filter = ['user']


@admin.register(OrderHistory)
class OrderHistoryAdmin(OrderBaseAdmin):
    list_display = ['id', 'product_name', 'size', 'quantity', 'single_price', 'user', 'specific_order_id',
                    'date_created']
    list_filter = ['date_created', 'user']
    date_hierarchy = 'date_created'
