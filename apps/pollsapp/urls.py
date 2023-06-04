from django.urls import path

from . import views

app_name = "pollsapp"
urlpatterns = [
    path("", views.IndexView.as_view(), name="index"),
    path("<int:pk>/<slug:question_slug>/",
         views.DetailView.as_view(), name="detail"),
    path("<int:pk>/<slug:question_slug>/results/",
         views.ResultsView.as_view(), name="results"),
    path("<int:question_id>/<slug:question_slug>/vote/",
         views.vote, name="vote"),
    path("new/",
         views.create_poll, name="new-poll"),
]
