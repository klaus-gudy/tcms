from django import forms
from django.forms import ModelForm

from .models import *

class CustomerForm(forms.ModelForm):
    account_name = forms.CharField(widget= forms.TextInput(attrs={'placeholder':'Add new customer '}))

    class Meta:
        model = Customer
        fields = '__all__'