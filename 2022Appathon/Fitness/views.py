from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect


def say_hello(request):
    return render(request, "Fitness/base.html")
