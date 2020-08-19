from django import forms
from .models import State, Senator, Senate_Bill

class StateForm(forms.ModelForm):
    class Meta:
        model = State
        fields = [
            "name"
        ]

class SenatorForm(forms.ModelForm):
    class Meta:
        model = Senator
        fields = [
            "name",
            "party",
            "voting_record"
        ]

class Senate_BillForm(forms.ModelForm):
    class Meta:
        model = Senate_Bill
        fields = [
            "name",
            "summary"
        ]