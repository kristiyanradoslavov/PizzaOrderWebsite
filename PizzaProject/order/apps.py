from django.apps import AppConfig


class OrderConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'PizzaProject.order'

    def ready(self):
        import PizzaProject.order.signals
