from django.contrib import admin

from PizzaProject.profiles.models import Profile


@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    pass
