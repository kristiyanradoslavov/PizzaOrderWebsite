from django.contrib import admin

from PizzaProject.order.models import OrderItem


@admin.register(OrderItem)
class OrderItemAdmin(admin.ModelAdmin):
    pass
