from django.db import models
from django.contrib.auth.models import User

class Book(models.Model):
    STATUS_CHOICES = [
        ('reading', 'Currently Reading'),
        ('completed', 'Completed'),
        ('wishlist', 'Wishlist'),
    ]
    
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=255)
    author = models.CharField(max_length=255)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='wishlist')

    def __str__(self):
        return self.title
