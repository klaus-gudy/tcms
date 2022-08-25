from django import forms
from django.forms import ModelForm

from .models import *

class BookForm(forms.ModelForm):
    name = forms.CharField(widget= forms.TextInput(attrs={'placeholder':'Add new book '}))

    class Meta:
        model = Book
        fields = '__all__'