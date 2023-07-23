from django.apps import AppConfig


class UserAuthenticationConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'PizzaProject.user_authentication'

    def ready(self):
        import PizzaProject.user_authentication.signals

