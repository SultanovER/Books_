from django.shortcuts import render
from .models import PostBooks
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from .models import PostBooks

class BookListView(ListView):
    model = PostBooks
    template_name = 'book_list.html'

class BookCreateView(CreateView):
    model = PostBooks
    fields = ['title', 'author', 'genre', 'year']
    template_name = 'book_form.html'
    success_url = '/books/'

class BookUpdateView(UpdateView):
    model = PostBooks
    fields = ['title', 'author', 'genre']
    template_name = 'book_form.html'
    success_url = '/books/'

class BookDeleteView(DeleteView):
    model = PostBooks
    template_name = 'book_confirm_delete.html'
    success_url = '/books/'

class SearchBooksView(ListView):
    model = PostBooks
    template_name = 'book_search_results.html'

    def get_queryset(self):
        query = self.request.GET.get('query')
        return PostBooks.objects.filter(title__icontains=query)

def book_list(request):
    books = PostBooks.objects.all()
    return render(request, 'books/book_list.html', {'books': books})
