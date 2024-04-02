from django import forms
from .models import review
from django.forms import ModelForm

# class reviewform(forms.Form):
#     first_name=forms.CharField(label='frist name',max_length=100)
#     last_name=forms.CharField(label='last name',max_length=100)
#     email=forms.EmailField(label='email')
#     review=forms.CharField(label='please enter review',widget=forms.Textarea(attrs={'class':'myform'}))





class reviewform(ModelForm):
    class Meta:
        model=review
        fields="__all__"
        # you can assignfields also ['first_name','last_name','star']

        labels={
            'first_name':'your first name',
            'last_name':'your last name',
            'star':'rating'
        }
        error={
            'max_value':'max value is 5',
            'min_value':'max value is 1',
        }