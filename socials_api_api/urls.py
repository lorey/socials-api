from django.urls import path

from . import views

app_name = "socials_api_api"

urlpatterns = [
    path("", views.api_root),
    path("filter-url", views.filter_url, name="filter-url"),
    path("filter-url-list", views.filter_url_list, name="filter-url-list"),
    path("fetch-url", views.fetch_url, name="fetch-url"),
]
