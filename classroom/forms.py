from django import forms
from django.forms import ModelForm
from .models import *

# class contactform(forms.Form):
#     name=forms.CharField(max_length=100)
#     messagge=forms.CharField(widget=forms.Textarea)

class contactform(ModelForm):
    class Meta:
        model=contact_info
        fields='__all__'
        labels={
            'name':'enter the name',
            'message':'enter the message'
        }

class teacher_info(ModelForm):
    class Meta:
        model=teacher
        fields='__all__'

        label={
            'first_name':'enter your first name ',
            'last_name':'enter your last name',
            'subject':'enter your subject'
        }

  