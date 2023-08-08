from PizzaProject import settings
from PizzaProject.order.models import OrderItem


def cart_count(request):
    cart_count = OrderItem.objects.filter(user_id=request.user.id).all()
    return {'cart_count': len(cart_count)}
