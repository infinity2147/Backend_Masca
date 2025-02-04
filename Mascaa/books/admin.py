from django.contrib import admin

# Register your models here.
from .models import book,Borrow_History
from backend.models import User

@admin.register(book)
class BookAdmin(admin.ModelAdmin):
    list_display = ('book_name', 'cover_page','author_name','published_year','subject','total_copies','available_copies','location')
    search_fields = ('book_name','author_name')
    
@admin.register(Borrow_History)
class Borrow_HistoryAdmin(admin.ModelAdmin):
    list_display = ('the_book', 'the_user', 'borrow_date', 'return_date')
    search_fields = ('the_book.book_name', 'the_user.Name')
    list_filter = ('borrow_date', 'return_date')