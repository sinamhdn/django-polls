from django.urls import path

from . import views

app_name = "polls"
urlpatterns = [
    path("", views.IndexView.as_view(), name="index"),
    path("<uuid:pk>/<slug:question_slug>/",
         views.DetailView.as_view(), name="detail"),
    path("<uuid:pk>/<slug:question_slug>/results/",
         views.ResultsView.as_view(), name="results"),
    path("<uuid:question_id>/<slug:question_slug>/vote/", views.vote, name="vote"),
]
