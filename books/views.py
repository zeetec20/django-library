from django.shortcuts import render
from .models import Book
import datetime

def index(request):
    context = {
        'bookAll': Book.objects.all()
    }
    if request.is_ajax():
        context['bookAll'] = Book.objects.all()
        return render(request, 'listBooks.html', context)

    if request.method == 'GET':
        return render(request, 'index.html', context)

def actionBooks(request):
    if request.method == 'GET':
        if request.is_ajax():
            if request.GET['action'] == 'update':
                number = (int(request.GET['book']) - 1)
                book = Book.objects.all()[number]
                date = book.publishDate
                print(date)
                context = {
                    'book': Book.objects.all()[number],
                    'bookPublishDate': date,
                    'bookNumber': int(request.GET['book'])
                }
                return render(request, 'update-add-book.html', context)
            elif request.GET['action'] == 'create':
                return render(request, 'update-add-book.html', {})

def saveBooks(request, action):
    if request.method == 'POST':
        if action == 'update':
            pass
        elif action == 'create':
            pass