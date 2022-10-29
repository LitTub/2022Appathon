from django import forms


class CreateClassroom(forms.Form):
    Time = forms.CharField(label="Subject", max_length=200)
    df = forms.CharField(label="Grade", max_length=2)
    NumOfStudents = forms.CharField(label="Number of Students", max_length=200)
    Favorite = forms.BooleanField(required=False)


class RunningCalculator(forms.Form):
    distance = forms.CharField(label="Distance", max_length=100)
    duration = forms.CharField(label="Duration", max_length=100)


INTENSITY = [
    ("low", "Low"),
    ("moderate", "Moderate"),
    ("high", "High"),
]


class SwimmingCalculator(forms.Form):
    duration = forms.CharField(label="Duration", max_length=100)
    intensity = forms.CharField(
        label="Intensity", widget=forms.Select(choices=INTENSITY))


class UpdateProfile(forms.Form):
    fullname = forms.CharField(max_length="100", required=False)
    age = forms.IntegerField(required=False)
    height = forms.IntegerField(required=False)
    weight = forms.IntegerField(required=False)
