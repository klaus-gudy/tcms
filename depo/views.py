from django.shortcuts import render, redirect

from django.views.generic import ListView, CreateView, DetailView, UpdateView,DeleteView

from .models import *

# Create your views here.
class DepositListView(ListView): 
    model = Deposit
    template_name ='depo/list.html'
    context_object_name = 'deposits'
    queryset = Deposit.objects.all()