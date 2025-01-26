from django.shortcuts import render, get_object_or_404,redirect
from .models import book, Rating, Review
from django.contrib import messages 
from django.contrib.auth.decorators import login_required
from .forms import ReviewForm


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
    return redirect('rate_and_review_book', book_id=Book.id)



def rate_and_review_book(request, book_id):
    the_book = get_object_or_404(book, id=book_id)

    if request.method == "POST":
        score = int(request.POST.get("score", 0))
        if 1 <= score <= 5:
            rating, created = Rating.objects.get_or_create(user=request.user, book=the_book)
            rating.score = score
            rating.save()
            
            if created:
                the_book.ratings_count += 1
                the_book.avg_rating = ((the_book.avg_rating * (the_book.ratings_count - 1)) + score) / the_book.ratings_count
            else:
                previous_score = rating.score
                the_book.avg_rating = ((the_book.avg_rating * the_book.ratings_count) - previous_score + score) / the_book.ratings_count

            the_book.save()

        # Handle review submission
        review_form = ReviewForm(request.POST)
        if review_form.is_valid():
            review = review_form.save(commit=False)
            review.book = the_book
            review.user = request.user
            review.save()

        return redirect('book_details', id=the_book.id)

    review_form = ReviewForm()
    return render(request, 'books/rate_and_review.html', {'the_book': the_book, 'review_form': review_form})
