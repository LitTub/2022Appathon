from django import forms


class CreateClassroom(forms.Form):
    Time = forms.CharField(label="Subject", max_length=200)
    = forms.CharField(label="Grade", max_length=2)
    NumOfStudents = forms.CharField(label="Number of Students", max_length=200)
    Favorite = forms.BooleanField(required=False)


class SetupForm(forms.Form):
    Weight = forms.CharField(label="Subject", max_length=200)
