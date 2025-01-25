from django.contrib import admin

# Register your models here.
from .models import book

@admin.register(book)
class BookAdmin(admin.ModelAdmin):
    list_display = ('book_name', 'author_name','published_year','is_available','subject','location')
    search_fields = ('book_name','author_name')