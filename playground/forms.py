# import the standard Django Forms
# from built-in library

from dataclasses import fields
from django import forms
from django.forms import ModelForm

from playground.models import Blog

#from playground import models

# creating a form


class InputForm(forms.Form):

    first_name = forms.CharField(max_length=200)
    last_name = forms.CharField(max_length=200)
    """roll_number = forms.IntegerField(
					help_text = "Enter 6 digit roll number"
					)"""
    id_number = forms.CharField(max_length = 200)
    password = forms.CharField(widget=forms.PasswordInput())


class CreateBlog(ModelForm):
    class Meta:
        model = Blog
        fields = ['title','body','photo']
