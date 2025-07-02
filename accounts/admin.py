from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from .models import User

# Register your models here.
@admin.register(User)
class UserAdmin(BaseUserAdmin):
    """Customizes the Django admin dashboard for the User model."""
    model = User
    # Show additional fields when changing users
    fieldsets = BaseUserAdmin.fieldsets + (
        ("Additional Info", {"fields": ("bio",)}),
    )
    # Show additional fields when Adding a new user
    add_fieldsets = BaseUserAdmin.add_fieldsets + (
        ("Additional Info", {"fields": ("bio",)}),
    )
    # Display bio columns in the table of users (optional)
    # list_display = UserAdmin.list_display + ("bio",)