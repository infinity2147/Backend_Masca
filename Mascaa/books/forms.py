
from django import forms
from .models import Review,Rating

class ReviewForm(forms.ModelForm):
    class Meta:
        model = Review
        fields = ['review_text']
        labels = {'review_text': 'Write a Review'}
        widgets = {'review_text': forms.Textarea(attrs={'placeholder': 'Write your review ', 'rows': 4})}


class RatingForm(forms.ModelForm):
    class Meta:
        model = Rating
        fields = ['score']
        labels = {'score': 'Rate this Book'}
        widgets = {'score': forms.Select(choices=[(i, f'{i} stars') for i in range(1, 6)]),}       

            