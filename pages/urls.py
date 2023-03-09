from django.urls import path

from .views import home_page_view

# Design your URL patterns here.

app_name = "pages"

urlpatterns = [
    path("", home_page_view, name="index"),
]
