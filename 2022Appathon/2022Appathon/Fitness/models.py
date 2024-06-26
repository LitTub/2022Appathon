from django.db import models
from django.contrib.auth.models import User
import datetime


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    fullname = models.CharField(max_length=50, default="")
    age = models.IntegerField(null=True)
    height = models.IntegerField(null=True)
    weight = models.IntegerField(null=True)


class Workout(models.Model):

    WORKOUT_TYPE = (
        ('Running', 'Running'),
        ('Biking', 'Biking'),
        ('Swimming', 'Swimming'),
    )

    user = models.ForeignKey(User, on_delete=models.CASCADE)
    fullname = models.CharField(default="", max_length=200)
    type = models.CharField(max_length=10, choices=WORKOUT_TYPE, blank=True)
    distance = models.IntegerField(default=0)
    duration = models.IntegerField()
    calories = models.IntegerField(default=0)
    date = models.DateField(default=datetime.datetime.now().date())

    class Meta:
        ordering = ['date']
