from django.db import models

# Create your models here.

class book(models.Model):
    book_name = models.CharField(max_length=200)
    author_name = models.CharField(max_length=100)
    cover_page = models.ImageField(blank=True)
    published_year = models.IntegerField()
    subject = models.CharField(max_length=50)  
    is_available= models.BooleanField(default= True)
    location = models.CharField(max_length=250)
    
    
    def __str__(self):
        return self.book_name