from django.urls import path, include
from . import views


urlpatterns = [
    path('home/', views.home),
    path('calculators/', views.calculators),
    path('profile/', views.profile)
]
