import imp
from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib import messages
from .forms import RunningCalculator, UpdateProfile, SwimmingCalculator
from . models import Workout, Profile
from django.core.exceptions import ObjectDoesNotExist
from django.contrib.auth import logout


def home(request):
    username = None
    if request.user.is_authenticated:
        user = request.user
        username = request.user.username
        workouts = Workout.objects.all()
        fields = {}
        for i in workouts:
            if i.user == user:
                attributes = list(i.__dict__.values())[1:]
                checkers = [field.name for field in Workout._meta.get_fields()]
                checkers = checkers[3:]
                attributes = attributes[3:]
                fields[getattr(i, "id")] = dict(zip(checkers, attributes))
        if not (fields):
            return render(request, "Fitness/home.html", {"username": username})
        fields = dict(reversed(list(fields.items())))
        if request.method == "POST":
            for i in range(1, 100):
                if str(i) in request.POST:
                    Workout.objects.get(id=i).delete()
                    return HttpResponseRedirect("/home/")

        return render(request, "Fitness/home.html", {"username": username, "fields": fields, "attributes": attributes})
    else:
        return HttpResponseRedirect("/signup")


def profile(request):
    user = None
    profile = None
    complete = False
    if request.user.is_authenticated:
        user = request.user
        try:
            Profile.objects.get(user=user)
        except ObjectDoesNotExist:
            Profile.objects.create(user=user)

        profile = Profile.objects.get(user=user)
        if profile.fullname != None and profile.age != None and profile.height != None and profile.weight != None:
            complete = True
        if request.method == "POST":
            form = UpdateProfile(request.POST)
            if form.is_valid():
                profile.fullname = form.cleaned_data["fullname"]
                profile.age = form.cleaned_data["age"]
                profile.height = form.cleaned_data["height"]
                profile.weight = form.cleaned_data["weight"]
                complete = True
                profile.save()
    else:
        return redirect("/signup")

    return render(request, "Fitness/profile.html", {"user": user, "profile": profile, "complete": complete})


def logoutUser(request):
    logout(request)
    return redirect("/login")


def runningcalc(request):
    if request.user.is_authenticated == False:
        return redirect("/signup")
    if request.method == "POST":
        form = RunningCalculator(request.POST)

        if form.is_valid():
            user = request.user
            profile = Profile.objects.get(user=user)
            workout = Workout()
            workout.user = user
            distance = form.cleaned_data["distance"]
            workout.distance = distance
            duration = form.cleaned_data["duration"]
            workout.duration = duration
            weight = profile.weight
            calories = calculate_cals_running(duration, distance, weight)
            workout.calories = calories
            workout.type = "Running"
            workout.save()
            return redirect("/home")

    else:
        form = RunningCalculator(request.POST)
    return render(request, "Fitness/running.html", {"form": form})


# BIKIGN


def bikingcalc(request):
    if request.method == "POST":
        form = RunningCalculator(request.POST)

        if form.is_valid():
            user = request.user
            profile = Profile.objects.get(user=user)
            workout = Workout()
            workout.user = user
            distance = form.cleaned_data["distance"]
            workout.distance = distance
            duration = form.cleaned_data["duration"]
            workout.duration = duration
            weight = profile.weight
            calories = calculate_cals_biking(duration, weight)
            workout.calories = calories
            workout.type = "Biking"
            workout.save()
            return redirect("/home")

    else:
        form = RunningCalculator(request.POST)
    return render(request, "Fitness/biking.html", {"form": form})


# SWIMIMNG


def swimmingcalc(request):
    if request.method == "POST":
        form = SwimmingCalculator(request.POST)

        if form.is_valid():
            user = request.user
            profile = Profile.objects.get(user=user)
            workout = Workout()
            workout.user = user
            duration = form.cleaned_data["duration"]
            workout.duration = duration
            weight = profile.weight
            workout.distance = 0
            intensity = form.cleaned_data["intensity"]
            calories = calculate_cals_swimming(duration, intensity, weight)
            workout.calories = calories
            workout.type = "Swimming"
            workout.save()
            return redirect("/home")

    else:
        form = SwimmingCalculator(request.POST)
    return render(request, "Fitness/swimming.html", {"form": form})


def calculate_cals_running(duration, distance, weight):
    weight_kg = weight/2.2
    pace = int(duration)/int(distance)
    met = 1.5
    pace_table = (60, 30, 24, 20, 18, 17, 15, 14, 13,
                  12, 11, 10, 9, 8.5, 8, 7.5, 7, 6.5, 0)
    met_table = (2, 2.5, 3, 3.5, 4, 4.5, 5, 6, 7, 8,
                 9, 10, 11, 12, 13, 14, 15, 16, 16)
    for i in range(len(pace_table)):
        if (pace <= pace_table[i] and pace > pace_table[i+1]):
            met = met_table[i]
            break
    calories = (int(duration) * met * weight_kg) / 60
    return int(calories)


def calculate_cals_biking(duration, weight):
    weight_kg = weight/2.2
    calories = (int(duration) * 6 * weight_kg) / 60
    return int(calories)


def calculate_cals_swimming(duration, intensity, weight):
    weight_kg = weight/2.2
    met = 6
    if (intensity == "low"):
        met = 6
    elif (intensity == "moderate"):
        met = 8.5
    elif (intensity == "high"):
        met = 12

    calories = (int(duration) * met * weight_kg) / 60
    return int(calories)
