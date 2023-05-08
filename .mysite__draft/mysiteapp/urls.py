from django.urls import path

from . import views

app_name = "mysiteapp"
urlpatterns = [
    path("", views.index, name="index"),
]
