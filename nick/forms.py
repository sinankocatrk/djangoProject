from django import forms 
from .models import Nick 


class NickForm(forms.ModelForm):
    class Meta:
        model = Nick
        fields = ["title","content"]
