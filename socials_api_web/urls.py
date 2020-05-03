from django.urls import path

from . import views

app_name = "socials_api_web"

urlpatterns = [path("", views.index, name="home")]
