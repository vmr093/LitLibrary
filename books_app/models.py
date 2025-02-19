from django.db import models
from django.contrib.auth.models import User

class Book(models.Model):
    STATUS_CHOICES = [
        ('reading', 'Currently Reading'),
        ('completed', 'Completed'),
        ('want to read ', 'Want to Read'),
    ]

    user = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=255)
    author = models.CharField(max_length=255)
    total_pages = models.IntegerField(default=0)
    current_page = models.IntegerField(default=0)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='wishlist')
    favorite = models.BooleanField(default=False)  # ✅ Favorite feature

    def __str__(self):
        return f"{self.title} by {self.author}"

class Review(models.Model):
    """Model to allow users to leave reviews on books."""
    book = models.ForeignKey(Book, on_delete=models.CASCADE, related_name="reviews")
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Review by {self.user.username} on {self.book.title}"