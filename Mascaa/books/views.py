from django.shortcuts import render, get_object_or_404,redirect
from .models import book
from django.contrib import messages 
from django.contrib.auth.decorators import login_required

def books(request):  
    books = book.objects.all()  # Fetch all books
    return render(request, 'books/book_list.html', {'books': books})

def book_details(request, book_id):
    the_book = get_object_or_404(book, pk=book_id)
    return render(request, 'books/book_details.html', {'the_book': the_book})

@login_required #to ensure that user is logged in

def take_book(request, book_id):
    Book = get_object_or_404(book, id=book_id)

    if Book.take_book(): 
        Book.is_available = Book.available_copies > 0
        Book.save()
        messages.success(request, f"You've successfully taken{Book.book_name}")
    else:
        messages.error(request, "Sorry, no copies are available to take.")
        
    return redirect('books')

def return_book(request, book_id):
    Book = get_object_or_404(book, id=book_id)

    if Book.return_book(): 
        Book.is_available = Book.available_copies > 0
        Book.save()
        messages.success(request, f"You've successfully returned the book {Book.book_name}")
    return redirect('books')
