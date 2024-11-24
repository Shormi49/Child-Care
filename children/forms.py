from django import forms
from .models import  Children


class ChildForm(forms.ModelForm):
    class Meta:
        model = Child
        fields = '__all__'
