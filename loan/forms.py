from .models import *
from django import forms

class LoanForm(forms.ModelForm):
    class Meta:
        model = loan
        fields = ['taken_from','amount']