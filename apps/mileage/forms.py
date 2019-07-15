from django import forms
from .models import Trip, Leg

class TripForm(forms.ModelForm):
    class Meta:
        model = Trip
        fields = ['name']

class LegCreate(forms.ModelForm):
    class Meta:
        model = Leg
        fields = ['start_date','start_miles']

class LegForm(forms.ModelForm):
    class Meta:
        model = Leg
        fields = ['start_date','start_miles','end_date','end_miles']
