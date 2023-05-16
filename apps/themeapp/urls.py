from django.urls import path

from . import views

app_name = "themeapp"
urlpatterns = [
    path("switchtheme", views.switchtheme, name="switchtheme"),
]
