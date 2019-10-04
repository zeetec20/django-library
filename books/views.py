from django.shortcuts import render
from .models import Book
from .forms import BookForm
import datetime
from django.http import JsonResponse
import copy

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
                valueBook = book.__dict__
                form = BookForm(initial = valueBook)

                context = {
                    'book': Book.objects.all()[number],
                    'formBook': form,
                    'bookNumber': int(request.GET['book'])
                }

                return render(request, 'update-add-book.html', context)
            elif request.GET['action'] == 'create':
                context = {
                    'formBook': BookForm(),
                }
                return render(request, 'update-add-book.html', context)

def saveBooks(request, action):
    if request.method == 'POST':
        if action == 'update':
            number = (int(request.POST['number']) - 1)
            book = Book.objects.all()[number],
            book = book[0]
            formBook = BookForm(request.POST)
            if formBook.is_valid():
                book.title = formBook.cleaned_data['title']
                book.author = formBook.cleaned_data['author']
                book.genre = formBook.cleaned_data['genre']
                book.publishDate = formBook.cleaned_data['publishDate']
                book.pages = formBook.cleaned_data['pages']
                book.price = formBook.cleaned_data['price']
                book.save()
            
            return JsonResponse({'success': True})
        elif action == 'add':
            formBook = BookForm(request.POST)
            if formBook.is_valid():
                formBook.save()
                return JsonResponse({'success': True})

def deleteBook(request, inputTitle):
    book = Book.objects.get(title = str(inputTitle))
    book.delete()
    
    return JsonResponse({'success': True})