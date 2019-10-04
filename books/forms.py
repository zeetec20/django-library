from django import forms
from .models import Book
from datetime import date

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

        dateNow = date.today().strftime('%Y-%m-%d')

        widgets = {
            'title': forms.TextInput(
                attrs = {
                    'class': 'form-control form-control-sm inputTitle',
                    'name': 'title',
                    'placeholder': 'Harry Potter and the Deathly Hallows'
                }
            ),
            'author': forms.TextInput(
                attrs = {
                    'class': 'form-control form-control-sm inputAuthor',
                    'name': 'author',
                    'placeholder': 'J. K. Rowling'
                }
            ),
            'genre': forms.TextInput(
                attrs = {
                    'class': 'form-control form-control-sm inputGenre',
                    'name': 'genre',
                    'placeholder': 'Action, Horror, Sci-Fi'
                }
            ),
            'publishDate': forms.DateInput(
                attrs = {
                    'class': 'form-control form-control-sm inputPublishDate',
                    'name': 'publishDate',
                    'placeholder': '"' + str(dateNow) + '"' + ' | year-month-day'
                }
            ),
            'pages': forms.NumberInput(
                attrs = {
                    'class': 'form-control form-control-sm inputPages',
                    'name': 'pages',
                    'placeholder': '400'
                }
            ),
            'price': forms.NumberInput(
                attrs = {
                    'class': 'form-control form-control-sm inputPrice',
                    'name': 'price',
                    'placeholder': '"500000" | IDR Rp500.000,00'
                }
            )
        }
