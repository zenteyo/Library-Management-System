from django.shortcuts import render

from django.shortcuts import render
from .models import Book

def book_list(request):
    books = Book.objects.all()  # Получить все книги из БД
    return render(request, 'library/book_list.html', {'books': books})