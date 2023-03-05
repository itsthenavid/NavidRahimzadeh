from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from .forms import CustomUserCreationForm, CustomUserChangeForm
from .models import CustomUser

# Register your models here.


@admin.register(CustomUser)
class CustomUserAdmin(UserAdmin):
    """
    This model is for the beautiful and correct display of the CustomUser 
    customized model in the management panel.

    In fact, this model is not a new class and it inherits from UserAdmin, 
    but it generally includes changes and those changes are also mentioned 
    in this class. How to display the list of users, change their profile, 
    access, etc. is determined in this class.
    """

    # Mention the updating of forms and the model
    add_form = CustomUserCreationForm
    form = CustomUserChangeForm
    model = CustomUser

    # Change decorations and customize commands
    list_display = (
        "get_user_avatar_thumbnail",
        "get_user_display_name",
        "nickname",
        "is_premium",
        "is_active",
        "is_staff",
        "is_superuser",
        "get_user_jalali_date_joined",
    )
    list_editable = (
        "nickname",
        "is_premium",
    )
    list_per_page = 10
    list_filter = (
        "is_premium",
        "is_active",
        "is_staff",
        "is_superuser",
    )
    search_fields = (
        "first_name",
        "last_name",
        "username",
        "nickname",
        "bio",
    )

    # Adapting fieldsets to new models and fields
    add_fieldsets = UserAdmin.add_fieldsets + (
        (
            None,
            {
                "fields": (
                    "email",
                    "avatar",
                    "first_name",
                    "last_name",
                    "nickname",
                    "bio",
                    "is_premium",
                    "is_active",
                    "is_staff",
                    "is_superuser",
                ),
            }, 
        ), 
    )
    fieldsets = UserAdmin.fieldsets + (
        (
            None, 
            {
                "fields": (
                    "avatar",
                    "nickname",
                    "bio",
                    "is_premium",
                ), 
            },
        ), 
    )
