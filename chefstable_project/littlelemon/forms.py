from django import forms

class Demoform(forms.Form):
    name = forms.CharField()