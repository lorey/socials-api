from django.urls import path

from . import views

app_name = "socials_api_api"

urlpatterns = [
    path("", views.api_root, name="root"),
    path("fetch-url", views.fetch_url, name="fetch-url"),
]
