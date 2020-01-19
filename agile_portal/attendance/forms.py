from django import forms
from django.contrib.gis.db import models
from django.core.exceptions import ValidationError


class employee_code(forms.Form):
    eID = forms.CharField(label='Your name', max_length=100) 

class getLocation(forms.Form):
    

    def clean_point(self):
        data = self.cleaned_data['point']
        return data