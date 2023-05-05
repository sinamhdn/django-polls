from django.http import Http404
from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
# // from django.template import loader

from .models import Question


def index(request):
    latest_question_list = Question.objects.order_by('-pub_date')[:5]
    context = {
        "latest_question_list": latest_question_list,
    }
    # // output = ", ".join([q.question_text for q in latest_question_list])
    # // return HttpResponse(output)
    # // template = loader.get_template("polls/index.html")
    # // return HttpResponse(template.render(context, request))
    return render(request, "polls/index.html", context)


def detail(request, question_id, question_slug):
    # //try:
    # //    question = Question.objects.get(pk=question_id)
    # //except Question.DoesNotExist:
    # //    raise Http404("Question does not exist")
    question = get_object_or_404(Question, hashed_id=question_id)
    return render(request, "polls/detail.html", {"question": question})


def results(request, question_id, question_slug):
    response = "You're looking at the results of question with id %s and slug %s."
    return HttpResponse(response % (question_id, question_slug))


def vote(request, question_id, question_slug):
    return HttpResponse("You're voting on question with id %s and slug %s." % (question_id, question_slug))
