from django.shortcuts import render ,  redirect
from django.http import HttpResponse

from .models import *
from .forms import *

# Create your views here.
def index(request):
    book = Book.objects.all()

    form = BookForm()

    if request.method == 'POST':
        form = BookForm(request.POST)
        if form.is_valid():
            form.save()
        
        return redirect('/')

    context = {'books': book,  'form':form}
    return render(request, 'base/list.html', context)


def update(request, pk):
    book  =  Book.objects.get(id=pk)

    form =  BookForm(instance=book)

    if request.method == 'POST':
        form = BookForm(request.POST, instance=book)
        if form.is_valid():
            form.save()
            return redirect('/')
        
        
    context = {'form':form}
    return render(request, 'base/update.html', context)

def delete(request, pk):
    item = Book.objects.get(id= pk)

    if request.method == 'POST':
        item.delete()
        return redirect('/')

    context = {'item':item}
    return render(request, 'base/delete.html', context)