from django.contrib.admin.views.decorators import staff_member_required
from django.shortcuts import render, get_object_or_404
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.db.models import F

from .models import Question, Choice


def index(request):
    latest_question_list = Question.objects.order_by('-pub_date')[:5]
    context = {
        "latest_question_list": latest_question_list,
    }
    return render(request, "polls/index.html", context)


def detail(request, question_id, question_slug):
    question = get_object_or_404(Question, hashed_id=question_id)
    return render(request, "polls/detail.html", {"question": question})


def results(request, question_id, question_slug):
    question = get_object_or_404(Question, hashed_id=question_id)
    return render(request, "polls/results.html", {"question": question})


# This decorator is used on the admin views that require authorization. A view decorated with this function will have the following behavior:
# If the user is logged in, is a staff member (User.is_staff=True), and is active (User.is_active=True), execute the view normally.
# Otherwise, the request will be redirected to the URL specified by the login_url parameter, with the originally requested path in a query string variable specified by redirect_field_name. For example: /admin/login/?next=/admin/polls/question/3/.
@staff_member_required
def vote(request, question_id, question_slug):
    question = get_object_or_404(Question, hashed_id=question_id)
    try:
        selected_choice = question.choice_set.get(pk=request.POST["choice"])
    except (KeyError, Choice.DoesNotExist):
        # Redisplay the question voting form.
        return render(
            request,
            "polls/detail.html",
            {
                "question": question,
                "error_message": "You didn't select a choice.",
            },
        )
    else:
        selected_choice.votes = F('votes') + 1
        selected_choice.save()
        return HttpResponseRedirect(reverse("polls:results", args=(question.hashed_id, question.slug,)))
