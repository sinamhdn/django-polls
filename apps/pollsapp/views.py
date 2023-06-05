from django.contrib.auth.decorators import login_required
from django.shortcuts import render, get_object_or_404, get_list_or_404
from django.http import HttpResponseRedirect
from django.utils import timezone
from django.views import generic
from django.urls import reverse
from django.db.models import F

from .models import Question, Choice, QuestionUser
from .forms import QuestionForm, ChoiceFormSet


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

    def get_context_data(self, **kwargs):
        context = super(DetailView, self).get_context_data(**kwargs)
        context['user'] = self.object.user
        # context['user'] = self.request.user
        return context

    # def get(self, request):
    #     if voted_before:
    #         return HttpResponseRedirect(reverse("pollsapp:results", args=(question.id, question.slug)))


class ResultsView(generic.DetailView):
    model = Question
    template_name = "pollsapp/results.html"

    def get_context_data(self, **kwargs):
        context = super(ResultsView, self).get_context_data(**kwargs)
        total_votes = 0
        for choice in self.object.choice_set.all():
            total_votes += choice.votes
        context['total_votes'] = total_votes
        context['user'] = self.object.user
        # context['user'] = self.request.user
        return context


@login_required(login_url='login')
def vote(request, question_id, question_slug):
    voted_before = True
    question = get_object_or_404(Question, id=question_id)
    user = request.user
    try:
        get_list_or_404(QuestionUser, question_id=question.id, user_id=user.id)
    except:
        voted_before = False
    # for question_user in question_users:
    #     if question_user.user_id == user.id:
    #         voted_before = True

    try:
        selected_choice = question.choice_set.get(
            pk=request.POST["choice"])
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
        if not voted_before:
            selected_choice.votes = F('votes') + 1
            question.total_votes = F('total_votes') + 1
            question_user = QuestionUser(
                question_id=question.id, user_id=user.id)
            question_user.save()
            selected_choice.save()
            question.save()
            return HttpResponseRedirect(reverse("pollsapp:results", args=(question.id, question.slug)))
    return render(
        request,
        "pollsapp/detail.html",
        {
            "question": question,
            "voted_before": voted_before,
            "error_message": "You have voted on this question before.",
        }
    )


@login_required(login_url='login')
def create_poll(request):
    question_form = QuestionForm(request.POST or None, request.FILES or None)
    choice_formset = ChoiceFormSet(request.POST or None, request.FILES or None)
    if request.method == 'POST':
        if all([question_form.is_valid(), choice_formset.is_valid()]):
            question = question_form.save(commit=False)
            choice_list = choice_formset.save(commit=False)
            question.user_id = request.user.id
            question.save()
            for choice in choice_list:
                choice.question_id = question.id
                choice.save()
            return HttpResponseRedirect(reverse('pollsapp:index'))
    return render(request, "pollsapp/poll_create_or_update.html", {"question_form": question_form, "choice_formset": choice_formset})


@login_required(login_url='login')
def edit_poll(request, question_id, question_slug):
    cur_question = Question.objects.get(id=question_id)
    # cur_choicesets = Choice.objects.filter(question_id=question_id)
    question_form = QuestionForm(
        request.POST or None, request.FILES or None, instance=cur_question)
    choice_formset = ChoiceFormSet(
        request.POST or None, request.FILES or None, instance=cur_question)
    if request.method == 'POST':
        if all([question_form.is_valid(), choice_formset.is_valid()]):
            question = question_form.save(commit=False)
            choice_list = choice_formset.save(commit=False)
            question.user_id = request.user.id
            question.save()
            for choice in choice_list:
                choice.question_id = question.id
                choice.save()
            return HttpResponseRedirect(reverse('pollsapp:index'))
    return render(request, "pollsapp/poll_create_or_update.html", {"question_form": question_form, "choice_formset": choice_formset})


@login_required(login_url='login')
def delete_poll(request, question_id, question_slug):
    question_form = QuestionForm(request.POST or None, request.FILES or None)
    choice_formset = ChoiceFormSet(request.POST or None, request.FILES or None)
    if request.method == 'POST':
        if all([question_form.is_valid(), choice_formset.is_valid()]):
            question = question_form.save(commit=False)
            choice_list = choice_formset.save(commit=False)
            question.user_id = request.user.id
            question.save()
            for choice in choice_list:
                choice.question_id = question.id
                choice.save()
            return HttpResponseRedirect(reverse('pollsapp:index'))
    return render(request, "pollsapp/poll_create_or_update.html", {"question_form": question_form, "choice_formset": choice_formset})
