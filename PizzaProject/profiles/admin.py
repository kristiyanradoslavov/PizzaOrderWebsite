from django.contrib import admin

from PizzaProject.profiles.models import Profile


@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    list_display = ['user_id', 'first_name', 'last_name', 'phone_number', 'address', 'user']
    list_display_links = ['user_id', 'first_name']
    search_fields = ['user_id', 'phone_number', 'user']
    search_help_text = 'Search by one of the following: User ID, Phone Number or Connected user email'
    list_filter = ['user']
    fieldsets = (
        ('User Connection', {
            'fields': ('user',)
        }),
        ('Personal Information', {
            'fields': ('first_name', 'last_name', 'image')
        }),
        ('Contact Information', {
            'fields': ('phone_number', 'city', 'address')
        }),
    )
