from django.shortcuts import render
from .models import PostBooks

def book_list(request):
    books = PostBooks.objects.all()
    return render(request, 'books/book_list.html', {'books': books})
