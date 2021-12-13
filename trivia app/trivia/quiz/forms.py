from django import forms
from .models import Name 
from django.forms.models import ALL_FIELDS, ModelForm


class UserCreateForm(forms.ModelForm):
    class Meta:
        model=Name
        fields=[ 'name' ]
       
