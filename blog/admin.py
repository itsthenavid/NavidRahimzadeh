from django.contrib import admin

from .models import Category, Post

# Register your models here.


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    """
    This class is written to display Category model information in 
    an orderly manner.
    """
    list_display = (
        "name",
        "is_active",
    )
    list_filter = (
        "is_active",
    )
    search_fields = (
        "title",
        "content",
    )


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    """
    This class is for customizing the Post model in the admin panel. The 
    information of this class should be very detailed and accurate and 
    support the solar/Jalali calendar model. This class is required to 
    allow editing of important information in the list view.

    Part of the design of this model is carried out by SRS and the rest of 
    the unit is carried out by the choice of the developer.
    """

    list_display = (
        "get_post_banner_thumbnail",
        "title",
        "category",
        "get_jalali_pub_datetime",
        "status",
        "is_active",
    )
    list_editable = (
        "category",
        "status",
    )
    list_filter = (
        "pub_datetime",
        "status",
        "is_active",
        "category",
        "tags",
    )
    search_fields = (
        "title",
        "description",
        "content",
    )
