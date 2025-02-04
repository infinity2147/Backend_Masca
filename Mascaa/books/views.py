from django.shortcuts import render, get_object_or_404,redirect
from .models import book, Rating, Review,Borrow_History
from backend.models import User
from django.contrib import messages 
from django.contrib.auth.decorators import login_required
from .forms import ReviewForm,RatingForm,BookForm
from django.utils import timezone


def books(request):  
    books = book.objects.all()  # Fetch all books
    return render(request, 'books/book_list.html', {'books': books})

def book_details(request, book_id):
    the_book = get_object_or_404(book, pk=book_id)
    
    reviews = the_book.reviews.all()  
    ratings = the_book.ratings.all() 
    
    user_reviewed = None
    user_rated = None
    user_review = None
    user_rating = None

    if request.user.is_authenticated:
        # Check if the user has already written a review
        user_review = Review.objects.filter(the_book=the_book, the_user=request.user).first()
        user_reviewed = user_review is not None

        # Check if the user has already rated
        user_rating = Rating.objects.filter(the_book=the_book, the_user=request.user).first()
        user_rated = user_rating is not None

    if request.method == 'POST' and request.user.is_authenticated:
        # Handling Review Submission
        if 'review' in request.POST and not user_reviewed: 
            review_form = ReviewForm(request.POST)
            if review_form.is_valid():
                review = review_form.save(commit=False)
                review.the_book = the_book
                review.the_user = request.user
                review.save()
                messages.success(request, "Your review has been submitted!")
                return redirect('book_details', book_id=the_book.id)

        # Handling Rating Submission
        if 'rating' in request.POST and not user_rated:
            rating_form = RatingForm(request.POST)
            if rating_form.is_valid():
                rating = rating_form.save(commit=False)
                rating.the_book = the_book
                rating.the_user = request.user
                rating.save()
                the_book.new_avg_rating(rating.score)
                messages.success(request, "Your rating has been submitted!")
                return redirect('book_details', book_id=the_book.id)

    else:
        review_form = ReviewForm()
        rating_form = RatingForm()
    
    return render(request, 'books/book_details.html', {
        'the_book': the_book,
        'reviews': reviews,
        'ratings': ratings,
        'review_form': review_form,
        'rating_form': rating_form,
        'user_reviewed': user_reviewed,
        'user_review': user_review,
        'user_rated': user_rated,
        'user_rating': user_rating,
        
    })  
        
    
        
@login_required #to ensure that user is logged in

def take_book(request, book_id):
    Book = get_object_or_404(book, id=book_id)
    user = request.user 

    if Book.take_book(): 
        Borrow_History.objects.create(
        the_book=Book,
        the_user=user,
        borrow_date=timezone.now(),
    )
        messages.success(request, f"You've successfully taken{Book.book_name}")
    else:
        messages.error(request, "Sorry, no copies are available to take.")
        
    return redirect('book_details',book_id=Book.id)

def return_book(request, book_id):
    Book = get_object_or_404(book, id=book_id)
    user = request.user
    # Find the borrow history record for this book that is not yet returned
    borrow_history = Borrow_History.objects.filter(the_book=Book, the_user=user, return_date__isnull=True).first()
    if Book.return_book(): 
        borrow_history.return_date = timezone.now()
        borrow_history.save()
        messages.success(request, f"You've successfully returned the book {Book.book_name}")
    return redirect('book_details', book_id=Book.id)



# @libadmin_required
def add_book(request):
    if request.method == 'POST':
        form = BookForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, "The book has been added successfully!")
            return redirect('books')  # Redirect to the manage books page
    else:
        form = BookForm()
    
    return render(request, 'add_book.html', {'form': form})