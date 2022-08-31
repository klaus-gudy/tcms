from django.shortcuts import render, redirect
from django.views.generic import ListView, CreateView, DetailView, UpdateView,DeleteView

from .models import *
from .forms import *

# Create your views here.

class CustomerListView(ListView): 
    model = Customer
    template_name ='cust/list.html'
    context_object_name = 'customers'
    queryset = Customer.objects.all()

class CustomerUpdateView(UpdateView):
    model = Customer
    template_name = 'cust/update.html' 
    context_object_name = 'customer'
    fields = ['account_number','account_name','address','age','acc_type']
    success_url = '/customer'

class CustomerDetailView(DetailView):
    model = Customer
    template_name = 'cust/detail.html' 
    context_object_name = 'customer'
    fields = ['account_number','account_name','address']

class CustomerCreateView(CreateView): 
    form_class = CustomerForm
    template_name = 'cust/create.html'
    context_object_name = 'customer'
    success_url = '/customer'

class CustomerDeleteView(DeleteView): 
    model = Customer
    template_name = 'cust/delete.html'
    context_object_name = 'customer'
    success_url = '/customer'