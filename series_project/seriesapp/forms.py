from django import forms

from.models import tvseries

class seriesform(forms.ModelForm):
    class Meta:
        model=tvseries
        fields=['name','desc','year','img']
