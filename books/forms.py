from django import forms
from .models import Book

class BookForm(forms.ModelForm):
    
    class Meta:
        model = Book
        fields = (
            "title",
            "author",
            "genre",
            "publishDate",
            "pages",
            "price"
        )

        widgets = {
            'title': forms.TextInput(
                attrs = {
                    'class': 'form-control form-control-sm inputTitle',
                    'name': 'title'
                }
            ),
            'author': forms.TextInput(
                attrs = {
                    'class': 'form-control form-control-sm inputAuthor',
                    'name': 'author'
                }
            ),
            'genre': forms.TextInput(
                attrs = {
                    'class': 'form-control form-control-sm inputGenre',
                    'name': 'genre'
                }
            ),
            'publishDate': forms.DateInput(
                attrs = {
                    'class': 'form-control form-control-sm inputPublishDate',
                    'name': 'publishDate'
                }
            ),
            'pages': forms.NumberInput(
                attrs = {
                    'class': 'form-control form-control-sm inputPages',
                    'name': 'pages'
                }
            ),
            'price': forms.NumberInput(
                attrs = {
                    'class': 'form-control form-control-sm inputPrice',
                    'name': 'price'
                }
            )
        }
