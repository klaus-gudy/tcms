from django import forms
from django.forms import ModelForm

from .models import *

from django.urls import reverse_lazy
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Row, Div, ButtonHolder, Button, Submit, Column

class CustomerForm(forms.ModelForm):

    class Meta:
        model = Customer
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        
        self.helper = FormHelper(self)
        self.helper.form_id = 'customer-create-form'
        self.helper.form_class = 'customer-create-form'
        self.helper.use_custom_control = True
        self.helper.form_tag = True
        self.helper.form_action = reverse_lazy('customer_create')
        self.helper.form_method = 'POST'

        self.helper.layout = Layout(
            Row(
                Div('account_number', css_class='col-md-6'),
                Div('account_name', css_class='col-md-6'),
                Div('address', css_class='col-md-12')
            ),
            ButtonHolder(
                Submit('submit', 'save', css_class='btn btn-success', css_id='btn-save-customer'),
                Button('cancel', 'Cancel', css_class='btn btn-danger', css_id='btn-cancel')
            )
        )

