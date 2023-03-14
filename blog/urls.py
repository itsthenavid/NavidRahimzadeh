from django.urls import path

from .views import post_list_view, post_detail_view

# Write URL Patterns here.

app_name = "blog"

urlpatterns = [
    path("", post_list_view, name="post_list"),
    path("<slug:slug>/", post_detail_view, name="post_detail"),
]
