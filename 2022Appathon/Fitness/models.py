from django.db import models
from django.contrib.auth.models import User
import datetime


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    fullname = models.CharField(max_length=50, default="")
    age = models.IntegerField()
    height = models.IntegerField()
    weight = models.IntegerField()


class Workout(models.Model):

    WORKOUT_TYPE = (
        ('r', 'Running'),
        ('b', 'Biking'),
        ('s', 'Swimming'),
    )

    user = models.ForeignKey(User, on_delete=models.CASCADE)
    type = models.CharField(max_length=1, choices=WORKOUT_TYPE, blank=True)
    duration = models.IntegerField()
    calories = models.IntegerField()
    date = models.DateField(default=datetime.datetime.now().date())

    class Meta:
        ordering = ['date']
