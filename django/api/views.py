from django.shortcuts import render
from books.models import Book
from rest_framework import viewsets
from .serializers import BookSerializer

class BookViewSet(viewsets.ModelViewSet):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
