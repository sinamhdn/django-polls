from django.urls import path

from . import views

app_name = "app_wsite"
urlpatterns = [
    path("", views.index, name="index"),
]
