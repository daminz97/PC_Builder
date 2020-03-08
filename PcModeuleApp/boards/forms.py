from django import forms
from .models import PC


class NewPcForm(forms.ModelForm):
    class Meta:
        model = PC
        fields = ['name', 'cpu', 'gpu', 'motherboard', 'ram', 'ssd', 'hdd']
