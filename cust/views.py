from django.shortcuts import render, redirect
from django.views.generic import ListView, CreateView, DetailView, UpdateView,DeleteView

from .models import *
from .forms import *

from django.contrib.messages.views import SuccessMessageMixin

from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin

from django.contrib.auth.views import redirect_to_login

class UserAccessMixin(PermissionRequiredMixin):
    def dispatch(self, request, *args, **kwargs):
        if(not self.request.user.is_authenticated):
            return redirect_to_login(
                self.request.get_full_path(),
                self.get_login_url(),
                self.get_redirect_field_name()
            )
        if not self.has_permission():
            return redirect('/customer')
        return super(UserAccessMixin, self).dispatch(request, *args, **kwargs)

class CustomerListView(LoginRequiredMixin, ListView):
    model = Customer
    template_name ='cust/list.html'
    context_object_name = 'customers'
    queryset = Customer.objects.all()

class CustomerUpdateView(UserAccessMixin, LoginRequiredMixin, SuccessMessageMixin,UpdateView):
    raise_exception = False
    permission_required = 'cust.change_customer'
    login_url = reverse_lazy('customer_list')


    form_class = CustomerForm
    model = Customer
    template_name = 'cust/update.html'
    context_object_name = 'customer'
    success_url = reverse_lazy('customer_list')
    success_message = "user has been updated"
    

class CustomerDetailView(UserAccessMixin, LoginRequiredMixin, DetailView):
    raise_exception = False
    permission_required = 'cust.view_customer'
    permission_denied_message = ''
    login_url = reverse_lazy('customer_list')
    redirect_field_name = 'next'

    model = Customer
    template_name = 'cust/detail.html' 
    context_object_name = 'customer'
    fields = ['account_number','account_name','address']

class CustomerCreateView(UserAccessMixin, LoginRequiredMixin, SuccessMessageMixin, CreateView): 
    raise_exception = False
    permission_required = 'cust.add_customer'
    permission_denied_message = ''
    login_url = reverse_lazy('customer_list')
    redirect_field_name = 'next'

    form_class = CustomerForm
    template_name = 'cust/create.html'
    context_object_name = 'customer'
    success_url = reverse_lazy('customer_list')
    success_message = "added a user"

class CustomerDeleteView(UserAccessMixin, LoginRequiredMixin, SuccessMessageMixin, DeleteView): 
    raise_exception = False
    permission_required = 'cust.delete_customer'
    permission_denied_message = ''
    login_url = reverse_lazy('customer_list')
    redirect_field_name = 'next'

    model = Customer
    template_name = 'cust/delete.html'
    context_object_name = 'customer'
    success_url = reverse_lazy('customer_list')
    success_message = "User has been deleted"