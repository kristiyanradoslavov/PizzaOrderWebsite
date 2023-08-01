from PizzaProject.order.models import OrderItem


def clear_order_items(user_id):
    all_ordered_items = OrderItem.objects.filter(user_id=user_id).all()
    all_ordered_items.delete()
