from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib import messages
from .forms import RunningCalculator
from . models import Workout


def home(request):
    username = None
    if request.user.is_authenticated:
        username = request.user.username

    return render(request, "Fitness/home.html", {"username": username})


def profile(request):
    user = None
    if request.user.is_authenticated:
        user = request.user
    return render(request, "Fitness/profile.html", {"user": user})


def calculators(request):
    if request.method == "POST":
        form = RunningCalculator(request.POST)

        if form.is_valid():
            values = form.cleaned_data
            workout = Workout()

            workout.save()

    else:
        form = RunningCalculator(request.POST)
    return render(request, "Fitness/calculators.html", {"form": form})
