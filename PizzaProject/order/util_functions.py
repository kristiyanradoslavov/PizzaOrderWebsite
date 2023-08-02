import uuid

from PizzaProject.order.models import OrderItem, OrderHistory


def clear_order_items(user_id):
    all_ordered_items = OrderItem.objects.filter(user_id=user_id).all()
    all_ordered_items.delete()


def create_order_history_item(user_id):
    all_ordered_items = OrderItem.objects.filter(user_id=user_id).all()
    specific_id = generate_unique_id()

    for current_order in all_ordered_items:
        OrderHistory.objects.create(
            product_name=current_order.product_name,
            product_id=current_order.product_id,
            quantity=current_order.quantity,
            size=current_order.size,
            single_price=current_order.single_price,
            image=current_order.image,
            user_id=user_id,
            price_id=current_order.price_id,
            specific_order_id=specific_id
        )


def generate_unique_id():
    return str(uuid.uuid4().hex)
