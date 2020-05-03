from django.urls import path

from . import views

app_name = "socials_api_api"

urlpatterns = [
    path('', views.index)
]
