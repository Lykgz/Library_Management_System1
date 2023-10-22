from django.urls import path
from . import views

urlpatterns = [
    path('books/', views.book_list, name='book_list'),
    path('add_book/', views.add_book, name='add_book'),
    path('edit_book/<str:isbn>/', views.edit_book, name='edit_book'),
    path('delete_book/<str:isbn>/', views.delete_book, name='delete_book'),
]
