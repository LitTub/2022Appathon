from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate
from .forms import SignupForm
# Create your views here.


def signup(request):
    if request.method == "POST":
        form = SignupForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("/hello")
    else:
        form = SignupForm()
    return render(request, "signup/signup.html", {"form": form})
