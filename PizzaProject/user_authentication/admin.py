from django.contrib import admin
from django.contrib.auth import get_user_model

UserModel = get_user_model()


@admin.register(UserModel)
class UserAdmin(admin.ModelAdmin):
    list_display = ['id', 'email', 'is_staff', 'is_active', 'is_superuser', 'date_joined', 'last_login']
    list_display_links = ['id', 'email']
    search_fields = ['email']
    search_help_text = 'Search by email'
    list_filter = ['date_joined', 'is_staff', 'is_active']

    fieldsets = (
        ('User Info', {
            'fields': ('email', 'password')
        }),
        ('Permissions and Groups', {
            'fields': ('user_permissions', 'groups')
        }),
        ('Other information', {
            'fields': ('is_superuser', 'is_staff', 'is_active', 'last_login')
        }),
    )
