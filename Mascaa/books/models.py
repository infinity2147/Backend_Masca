from django.db import models
from backend.models import User


# Create your models here.

class book(models.Model):
    book_name = models.CharField(max_length=200)
    author_name = models.CharField(max_length=100)
    cover_page = models.ImageField(upload_to='cover_page/',default='cover_page/67d525a6-7901-4ee3-b0f8-3a4cf020a0de.webp')
    published_year = models.IntegerField()
    subject = models.CharField(max_length=50)  
    total_copies = models.IntegerField(default=1)
    available_copies=models.IntegerField(default=total_copies)
    location = models.CharField(max_length=250)
    avg_rating = models.FloatField(default=None)
    ratings_count = models.PositiveIntegerField(default=0)
    
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
    
    def new_avg_rating(self,new_point):
        self.ratings_count += 1
        self.avg_rating = ((self.avg_rating * (self.ratings_count - 1)) + new_point ) / self.ratings_count
        self.save()
    
class Rating(models.Model):
    the_book = models.ForeignKey(book, related_name="ratings", on_delete=models.CASCADE)
    the_user = models.ForeignKey(User, on_delete=models.CASCADE)
    score = models.PositiveSmallIntegerField(choices=[(i,i) for i in range(1,6)])  
    rated_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        unique_together = ('the_book', 'the_user')
        

    def __str__(self):
        return f'{self.the_user.username} rated {self.the_book.book_name} - {self.score}'
    
        
        
    
class Review(models.Model):
    the_book = models.ForeignKey(book, related_name="reviews", on_delete=models.CASCADE)
    the_user = models.ForeignKey(User, on_delete=models.CASCADE)
    review_text = models.TextField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    
    class Meta:
        unique_together = ('the_book', 'the_user')

    def __str__(self):
        return f'{self.the_user.username} reviewed {self.the_book.book_name}'  


class Borrow_History(models.Model):
    the_book = models.ForeignKey(book, on_delete=models.CASCADE, related_name='borrow_history') 
    the_user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='borrowed_books')
    borrow_date = models.DateField(auto_now_add=True)  
    return_date = models.DateField(null=True, blank=True)  

    def __str__(self):
        return f"{self.user.Name} borrowed {self.book.title} on {self.borrow_date}"

    def mark_as_returned(self):
        self.return_date = models.DateField(auto_now=True)
        self.save()