from django import forms
from .models import Book, Review

class BookForm(forms.ModelForm):
    class Meta:
        model = Book
        fields = ['title', 'author', 'total_pages', 'current_page', 'status']


class ReviewForm(forms.ModelForm):
    class Meta:
        model = Review
        fields = ['content']
