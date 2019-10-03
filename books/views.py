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
                print(valueBook)
                form = BookForm(initial = valueBook)
                date = copy.deepcopy(book.publishDate)
                print(date)

                context = {
                    'book': Book.objects.all()[number],
                    'bookPublishDate': date,
                    'formBook': form,
                    'bookNumber': int(request.GET['book'])
                }

                return render(request, 'update-add-book.html', context)
            elif request.GET['action'] == 'create':
                return render(request, 'update-add-book.html', {})

def saveBooks(request, action):
    if request.method == 'POST':
        if action == 'update':
            number = (int(request.POST['number']) - 1)
            book = Book.objects.all()[number],
            book = book[0]
            book.title = request.POST['title']
            book.author = request.POST['author']
            book.genre = request.POST['genre']
            book.publishDate = request.POST['publishDate']
            book.pages = request.POST['pages']
            book.price = request.POST['price']
            book.save()
            return JsonResponse({'success': True})
        elif action == 'create':
            pass