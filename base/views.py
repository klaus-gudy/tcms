from django.shortcuts import render ,  redirect
from django.http import HttpResponse

from django.views.generic import ListView, CreateView, DetailView, UpdateView,DeleteView

from .models import *
from .forms import *



class BookListView(ListView): 
    model = Book
    template_name ='base/list.html'
    context_object_name = 'books'
    queryset = Book.objects.all()


class BookUpdateView(UpdateView):
    model = Book
    template_name = 'base/update.html' 
    context_object_name = 'books'
    fields = ['name']
    success_url = '/books'
        
        
class BookDetailView(DetailView):
    model = Book
    template_name = 'base/detail.html' 
    context_object_name = 'books'
    fields = ['name']

class BookCreateView(CreateView): 
    model = Book
    template_name = 'base/create.html'
    context_object_name = 'books'
    fields = ['name']
    success_url = '/books'

class BookDeleteView(DeleteView): 
    model = Book
    template_name = 'base/delete.html'
    context_object_name = 'book'
    success_url = '/books'