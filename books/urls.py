from django.urls import path, include
from .views import BookListView, SearchBooksView

urlpatterns = [
    path('books/', include('books.urls')),
    path('books/search/', SearchBooksView.as_view(), name='search_books'),

]
