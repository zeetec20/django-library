from django.contrib import admin
from django.urls import path, include
from rest_framework import routers
from books.views import (
    index, 
    actionBooks, 
    saveBooks, 
    deleteBook,
)
from api.views import BookViewSet

router = routers.DefaultRouter()
router.register(r'book', BookViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', index, name='index'),
    path('actionBooks', actionBooks, name='editBooks'),
    path('saveBooks/<str:action>', saveBooks, name='saveBooks'),
    path('deleteBooks/<str:inputTitle>', deleteBook, name='deleteBook'),
    path('api/', include(router.urls), name='api'),
]
