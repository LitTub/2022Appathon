from django.urls import path, include
from . import views


urlpatterns = [
    path('home/', views.home),
    path('calculators/running/', views.runningcalc),
    path('calculators/biking/', views.bikingcalc),
    path('calculators/swimming/', views.swimmingcalc),
    path('calculators/', views.runningcalc),
    path('profile/', views.profile)
]
