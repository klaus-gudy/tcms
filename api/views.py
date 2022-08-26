from django.shortcuts import render

# Create your views here.
from rest_framework.response import Response
from rest_framework.decorators import api_view

from base.models import Book
from .serializers import BookSerializer

@api_view(["get"])
def getBooks(request):
    books      = Book.objects.all()
    serializer = BookSerializer(books, many=True)
    return Response(serializer.data)

@api_view(["GET"])
def getDetailBook(request, pk):
    book       = Book.objects.get(id=pk)
    serializer = BookSerializer(book, many=False)
    return Response(serializer.data)

@api_view(["PUT"])
def updateBook(request,pk):
    book       = Book.objects.get(id=pk)
    serializer = BookSerializer(book, data=request.data)
    if serializer.is_valid():
        serializer.save()

    return Response(serializer.data)

@api_view(["POST"])
def createBook(request):
    data = request.data
    book       = Book.objects.create(
        body   = data['body']
    )
    serializer = NoteSerializer(book, many=False)
    return Response(serializer.data)

#create book api ina shida kidogo matengenezo yaitajika

@api_view(["DELETE"])
def deleteBook(request, pk):
    book  = Book.objects.get(id=pk)
    book.delete()
    return Response("Book Deleted")