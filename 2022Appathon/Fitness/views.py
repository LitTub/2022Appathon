from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib import messages


def home(request):
    username = None
    if request.user.is_authenticated:
        username = request.user.username

    return render(request, "Fitness/home.html", {"username": username})
