from django.shortcuts import render, get_object_or_404
from django.http import HttpResponseRedirect
from django.utils import timezone
from django.views import generic
from django.urls import reverse
from django.db.models import F

from .models import Question, Choice


class IndexView(generic.ListView):
    template_name = "pollsapp/index.html"
    context_object_name = "latest_question_list"

    def get_queryset(self):
        """Return the last five published questions."""
        return Question.objects.filter(pub_date__lte=timezone.now()).order_by("-pub_date")[:5]


class DetailView(generic.DetailView):
    model = Question
    template_name = "pollsapp/detail.html"

    def get_queryset(self):
        """
        Excludes any questions that aren't published yet.
        """
        return Question.objects.filter(pub_date__lte=timezone.now())


class ResultsView(generic.DetailView):
    model = Question
    template_name = "pollsapp/results.html"

    def get_context_data(self, **kwargs):
        context = super(ResultsView, self).get_context_data(**kwargs)
        total_votes = 0
        for choice in self.object.choice_set.all():
            total_votes += choice.votes
        context['total_votes'] = total_votes
        return context


def vote(request, question_id, question_slug):
    question = get_object_or_404(Question, id=question_id)
    try:
        selected_choice = question.choice_set.get(pk=request.POST["choice"])
    except (KeyError, Choice.DoesNotExist):
        # Redisplay the question voting form.
        return render(
            request,
            "pollsapp/detail.html",
            {
                "question": question,
                "error_message": "You didn't select a choice.",
            },
        )
    else:
        selected_choice.votes = F('votes') + 1
        question.total_votes = F('total_votes') + 1
        selected_choice.save()
        question.save()
        return HttpResponseRedirect(reverse("pollsapp:results", args=(question.id, question.slug)))
