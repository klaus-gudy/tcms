from django.shortcuts import render, redirect

from django.views.generic import ListView, CreateView, DetailView, UpdateView,DeleteView

from .models import *
from .forms import *

from django.contrib.auth.mixins import LoginRequiredMixin

# Create your views here.
class DepositListView(ListView): 
    model = Deposit
    template_name ='depo/list.html'
    context_object_name = 'deposits'
    queryset = Deposit.objects.all()

class GenerateToken(DetailView):
    model = Deposit
    template_name = 'depo/token.html' 
    context_object_name = 'deposit'
    fields = ['token']

class DepositView(LoginRequiredMixin,CreateView): 
    form_class = DepositForm
    template_name = 'depo/deposit.html'
    context_object_name = 'deposit'
    success_url = '/trans/history'

    def form_valid(self, form):
        form.instance.customer = self.request.user
        return super(DepositView, self).form_valid(form)