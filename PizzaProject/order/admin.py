from django.contrib import admin

from PizzaProject.order.models import OrderItem, OrderHistory


@admin.register(OrderItem)
class OrderItemAdmin(admin.ModelAdmin):
    list_display = ['id', 'product_name', 'size', 'quantity', 'single_price', 'user']
    search_fields = ['product_name', 'size']
    search_help_text = 'Search by Name of the product or Size.'
    list_filter = ['user']
    list_display_links = ['id', 'product_name']


@admin.register(OrderHistory)
class OrderItemAdmin(admin.ModelAdmin):
    list_display = ['id', 'product_name', 'size', 'quantity', 'single_price', 'user', 'specific_order_id',
                    'date_created']
    list_filter = ['date_created', 'user']
    search_fields = ['product_name', 'size']
    search_help_text = 'Search by Name of the product or Size.'
    actions = ['completed']
    list_display_links = ['id', 'product_name']
    date_hierarchy = 'date_created'

    fieldsets = (
        ('User Information', {
            'fields': ('user',)
        }),
        ('Product Information', {
            'fields': ('product_name', 'product_id', 'quantity', 'size', 'single_price', 'image', 'price_id')
        }),
    )
