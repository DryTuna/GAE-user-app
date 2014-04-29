'''
Created on Apr 28, 2014

@author: Duy Tran
'''
from django import forms
from models import People

class CreatePeopleForm(forms.ModelForm):
    class Meta:
        model = People