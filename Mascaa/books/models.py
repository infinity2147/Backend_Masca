from django.db import models

# Create your models here.

class book(models.Model):
    book_name = models.CharField(max_length=200)
    author_name = models.CharField(max_length=100)
    cover_page = models.ImageField(upload_to='cover_page/', blank=True, null=True)
    published_year = models.IntegerField()
    subject = models.CharField(max_length=50)  
    total_copies = models.IntegerField(default=1)
    available_copies=models.IntegerField(default=1)
    location = models.CharField(max_length=250)
    
    
    def __str__(self):
        return self.book_name
    
    def take_book(self):
        if self.available_copies > 0:
            self.available_copies -= 1
            self.save()
            return True
        return False
    def return_book(self):
        if self.available_copies < self.total_copies:
            self.available_copies += 1
            self.save()
            return True
        return False
    
    def is_available(self):
        return self.available_copies > 0
    
    
    def availability_status(self):
        return "Yes" if self.is_available() else "No"