from django.shortcuts import render, redirect
from django.views.generic import ListView, CreateView, DetailView, UpdateView,DeleteView

from .models import *
from .forms import *

from django.contrib.messages.views import SuccessMessageMixin

# Create your views here.

class CustomerListView(ListView): 
    model = Customer
    template_name ='cust/list.html'
    context_object_name = 'customers'
    queryset = Customer.objects.all()

class CustomerUpdateView(SuccessMessageMixin,UpdateView):
    form_class = CustomerForm
    model = Customer
    template_name = 'cust/update.html'
    context_object_name = 'customer'
    success_url = reverse_lazy('customer_list')
    success_message = "user has been updated"
    

class CustomerDetailView(DetailView):
    model = Customer
    template_name = 'cust/detail.html' 
    context_object_name = 'customer'
    fields = ['account_number','account_name','address']

class CustomerCreateView(SuccessMessageMixin, CreateView): 
    form_class = CustomerForm
    template_name = 'cust/create.html'
    context_object_name = 'customer'
    success_url = reverse_lazy('customer_list')
    success_message = "added a user"

class CustomerDeleteView(SuccessMessageMixin, DeleteView): 
    model = Customer
    template_name = 'cust/delete.html'
    context_object_name = 'customer'
    success_url = reverse_lazy('customer_list')
    success_message = "User has been deleted"