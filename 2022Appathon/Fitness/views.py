import imp
from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib import messages
from .forms import RunningCalculator, UpdateProfile
from . models import Workout, Profile
from django.core.exceptions import ObjectDoesNotExist


def home(request):
    username = None
    if request.user.is_authenticated:
        username = request.user.username
        workouts = Workout.objects.all()

    return render(request, "Fitness/home.html", {"username": username, "workouts": workouts})


def profile(request):
    user = None
    profile = None
    if request.user.is_authenticated:
        user = request.user
        try:
            Profile.objects.get(user=user)
        except ObjectDoesNotExist:
            Profile.objects.create(user=user)

        profile = Profile.objects.get(user=user)
        if request.method == "POST":
            form = UpdateProfile(request.POST)
            if form.is_valid():
                profile.fullname = form.cleaned_data["fullname"]
                profile.age = form.cleaned_data["age"]
                profile.height = form.cleaned_data["height"]
                profile.weight = form.cleaned_data["weight"]
                profile.save()

    return render(request, "Fitness/profile.html", {"user": user, "profile": profile})


def calculators(request):
    if request.method == "POST":
        form = RunningCalculator(request.POST)

        if form.is_valid():
            user = request.user
            profile = Profile.objects.get(user=user)
            workout = Workout()
            workout.user = user
            workout.fullname = profile.fullname
            workout.duration = form.cleaned_data["duration"]
            #workout.calories = form.cleaned_data["calories"]
            workout.save()

    else:
        form = RunningCalculator(request.POST)
    return render(request, "Fitness/running.html", {"form": form})
