from django.shortcuts import render, redirect

from pollsapp.models import Question


def index(request):
    featured_questions = Question.objects.all().filter(
        featured=True).order_by('pub_date')
    return render(request, "root/index.html", context={"featured_questions": featured_questions})
