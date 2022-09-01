from django import forms 
from .models import Nick,Comment 


class NickForm(forms.ModelForm):
    class Meta:
        model = Nick
        fields = ["title","content","article_image"]
