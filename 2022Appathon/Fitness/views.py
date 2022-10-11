from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib import messages


def home(request):
    return render(request, "Fitness/home.html")
