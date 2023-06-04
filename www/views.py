# from django.views.defaults import bad_request, page_not_found, server_error, permission_denied
# from django.core.exceptions import BadRequest,PermissionDenied
from django.shortcuts import render, redirect
from django.contrib.auth import login, logout, authenticate

from pollsapp.models import Question
from .forms import RegistrationForm


def error_400(request, exception):
    return render(request, 'root/400.html')


def error_403(request, exception):
    return render(request, 'root/403.html')


def error_404(request, exception):
    return render(request, 'root/404.html')


def error_500(request, *args, **argv):
    return render(request, 'root/500.html', status=500)


def test_400(request):
    return render(request, 'root/400.html')


def test_403(request):
    return render(request, 'root/403.html')


def test_404(request):
    return render(request, 'root/404.html')


def test_500(request):
    return render(request, 'root/500.html')


def index(request):
    featured_questions = Question.objects.all().filter(
        featured=True).order_by('pub_date')
    popular_questions = Question.objects.all().order_by('total_votes')[:10]
    return render(request, "root/index.html", context={"featured_questions": featured_questions, "popular_questions": popular_questions, "user": request.user})


def signup(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('home')
    else:
        form = RegistrationForm()
    return render(request, 'registration/signup.html', {"form": form})
