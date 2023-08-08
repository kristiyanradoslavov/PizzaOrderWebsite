from django.contrib import admin

from PizzaProject.order.models import OrderItem, OrderHistory


@admin.register(OrderItem)
class OrderItemAdmin(admin.ModelAdmin):
    list_display = ['id', 'product_name', 'size', 'quantity', 'single_price', 'user']
    search_fields = ['product_name', 'size']
    search_help_text = 'Search by Name of the product or Size.'
    list_filter = ['user']


@admin.register(OrderHistory)
class OrderItemAdmin(admin.ModelAdmin):
    list_display = ['id', 'product_name', 'size', 'quantity', 'single_price', 'user', 'specific_order_id',
                    'date_created']
    list_filter = ['date_created', 'user']
    search_fields = ['product_name', 'size']
    search_help_text = 'Search by Name of the product or Size.'
    actions = ['completed']

    def mark_as_completed(self, request, queryset):
        queryset.update(completed=True)

    mark_as_completed.short_description = 'Mark selected orders as completed'

    fieldsets = (
        ('General Information', {
            'fields': ('product_name', 'size'),
        }),
        ('Status', {
            'fields': ('completed',),
        }),
    )
