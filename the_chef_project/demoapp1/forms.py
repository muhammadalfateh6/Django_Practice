from django import forms
from .models import Customer_Table

shifts = (('1','Morning'),('2', 'Afternoon'),('3', 'Night'),)

# class DemoForm(forms.Form):
#     name = forms.CharField(max_length = 200)
#     las_name = forms.CharField(max_length = 100)
#     time_log = forms.TimeField()


class Customer_Form(forms.ModelForm):
    class Meta:
        model = Customer_Table
        fields = '__all__'


    