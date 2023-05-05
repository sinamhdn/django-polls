from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("<str:question_id>/<slug:question_slug>/",
         views.detail, name="detail"),
    path("<str:question_id>/<slug:question_slug>/results/",
         views.results, name="results"),
    path("<str:question_id>/<slug:question_slug>/vote/", views.vote, name="vote"),
]
