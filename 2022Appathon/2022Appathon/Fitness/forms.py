from django import forms

class RunningCalculator(forms.Form):
    distance = forms.CharField(label="Distance (miles)", max_length=100)
    duration = forms.CharField(label="Duration (mins)", max_length=100)


INTENSITY = [
    ("low", "Low"),
    ("moderate", "Moderate"),
    ("high", "High"),
]


class SwimmingCalculator(forms.Form):
    duration = forms.CharField(label="Duration (mins)", max_length=100)
    intensity = forms.CharField(
        label="Intensity", widget=forms.Select(choices=INTENSITY))


class UpdateProfile(forms.Form):
    fullname = forms.CharField(max_length="100", required=False)
    age = forms.IntegerField(required=False)
    height = forms.IntegerField(required=False)
    weight = forms.IntegerField(required=False)
