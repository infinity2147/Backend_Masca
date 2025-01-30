from django.urls import path
from . import views

urlpatterns=[
    path('books/',views.books,name='books'),
    path('books/<int:book_id>/',views.book_details,name='book_details'),
    path('book/<int:book_id>/take_book/', views.take_book, name='take_book'),
    path('book/<int:book_id>/return_book/', views.return_book, name='return_book'),
]
