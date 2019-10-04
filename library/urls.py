from django.contrib import admin
from django.urls import path
from books.views import (
    index, 
    actionBooks, 
    saveBooks, 
    deleteBook,
)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', index, name='index'),
    path('actionBooks', actionBooks, name='editBooks'),
    path('saveBooks/<str:action>', saveBooks, name='saveBooks'),
    path('deleteBooks/<str:inputTitle>', deleteBook, name='deleteBook'),
]
