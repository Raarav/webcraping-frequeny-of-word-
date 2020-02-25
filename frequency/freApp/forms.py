from django import forms
from .models import *

####url######
class freqform(forms.ModelForm):
    class Meta:
        model=freq
        fields="__all__"

####urlform#########