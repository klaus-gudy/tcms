from django import forms
from django.forms import ModelForm

from .models import *

from django.urls import reverse_lazy
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Row, Div, ButtonHolder, Button, Submit, Column

class DepositForm(forms.ModelForm):

    class Meta:
        model = Deposit
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        
        self.helper = FormHelper(self)
        self.helper.form_id = 'deposit'
        self.helper.form_class = 'deposit'
        self.helper.use_custom_control = True
        self.helper.form_tag = True
        self.helper.form_method = 'POST'

        self.helper.layout = Layout(

            Column(
                    Div('amount', css_class='col-md-6'),
                    Div('my_account', css_class='col-md-6'),
            ),

            ButtonHolder(
                Submit('submit', 'Deposit', css_class='btn btn-success', css_id='btn-deposit'),
                Button('cancel', 'Cancel', css_class='btn btn-danger', css_id='btn-cancel')
            )
        )
