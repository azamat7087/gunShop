from django import forms
from .models import *
from django.core.exceptions import ValidationError
from django_summernote.widgets import SummernoteWidget

class InfoOfUserForm(forms.ModelForm):
    class Meta:
        model = InfoOfUser
        fields = ['name', 'sex', 'image', 'date_of_birth', 'body', 'cash']
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control'}),
            'body': forms.Textarea(attrs={'class': 'form-control'}),
        }
