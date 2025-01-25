from django.shortcuts import render, get_object_or_404
from .models import book

def books(request):  
    books = book.objects.all()  # Fetch all books
    return render(request, 'books/book_list.html', {'books': books})

def book_details(request, book_id):
    the_book = get_object_or_404(book, pk=book_id)
    return render(request, 'books/book_details.html', {'book': book})
