from django import forms
from places.models import Place

class PlaceForm(forms.ModelForm):
    class Meta:
        model = Place
        fields = "__all__"
        widgets = {
            "name": forms.TextInput(attrs={"class": "form-control", "placeholder": "Enter name"}),
            "latitude": forms.TextInput(attrs={"class": "form-control", "placeholder": "Enter latitude"}),
            "longitude": forms.TextInput(attrs={"class": "form-control", "placeholder": "Enter longitude"}),
            "location": forms.TextInput(attrs={"class": "form-control", "placeholder": "Enter location"}),
        }
