from django.shortcuts import render, redirect


def index(request):
    return render(request, "root/index.html", context={'gohome': redirect('home')})
