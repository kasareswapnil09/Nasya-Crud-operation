# college/forms.py

from django import forms
from .models import Statistic

class StatisticForm(forms.ModelForm):
    class Meta:
        model = Statistic
        fields = ['title', 'value']  # Adjust the fields as per your model
