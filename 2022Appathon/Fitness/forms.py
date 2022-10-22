from django import forms


class CreateClassroom(forms.Form):
    Time = forms.CharField(label="Subject", max_length=200)
    df = forms.CharField(label="Grade", max_length=2)
    NumOfStudents = forms.CharField(label="Number of Students", max_length=200)
    Favorite = forms.BooleanField(required=False)


class RunningCalculator(forms.Form):
    Weight = forms.CharField(label="Weight", max_length=100)
    Distance = forms.CharField(label="Distance", max_length=100)
    Duration = forms.CharField(label="Duration", max_length=100)
