from rest_framework import serializers

from PizzaProject.order.models import OrderItem


class BaseItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = OrderItem
        fields = '__all__'


class OrderItemSerializer(BaseItemSerializer):
    class Meta:
        model = OrderItem
        fields = ['id', 'quantity']


class DeleteItemSerializer(BaseItemSerializer):
    pass


class CreateItemSerializer(BaseItemSerializer):
    pass


class GetItemsSerializer(BaseItemSerializer):
    pass
