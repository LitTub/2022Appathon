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

    return render(request, "Fitness/home.html", {"username": username})


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
            print(request.POST)
            print(form.is_valid())
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
            values = form.cleaned_data
            workout = Workout()

            workout.save()

    else:
        form = RunningCalculator(request.POST)
    return render(request, "Fitness/calculators.html", {"form": form})
