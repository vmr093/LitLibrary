import requests
from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth import login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from .models import Book, Review
from .forms import BookForm, ReviewForm, ProgressForm

# Google Books API Base URL
GOOGLE_BOOKS_API_URL = "https://www.googleapis.com/books/v1/volumes?q="


### 📌 USER AUTHENTICATION VIEWS ###

# Signup View
def signup(request):
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)  # Log the user in immediately after signup
            return redirect('book_list')  # Redirect to books list after signing up
    else:
        form = UserCreationForm()
    return render(request, 'books_app/signup.html', {'form': form})


# Custom Logout View (Allows GET Request)
def custom_logout(request):
    logout(request)
    return redirect('login')


### 📌 BOOK MANAGEMENT VIEWS ###

# List all books for the logged-in user
@login_required
def book_list(request):
    books = Book.objects.filter(user=request.user)
    return render(request, 'books_app/book_list.html', {'books': books})


# Add a new book with details fetched from Google Books API
@login_required
def book_create(request):
    if request.method == "POST":
        form = BookForm(request.POST)
        if form.is_valid():
            book = form.save(commit=False)
            book.user = request.user
            query = f"{book.title} {book.author}"
            response = requests.get(f"{GOOGLE_BOOKS_API_URL}{query}")
            data = response.json()

            # Fetch book cover image from API
            if "items" in data:
                book.cover_image = data["items"][0]["volumeInfo"].get("imageLinks", {}).get("thumbnail", "")

            book.save()
            return redirect('book_list')
    else:
        form = BookForm()
    return render(request, 'books_app/book_form.html', {'form': form})


# Update book details
@login_required
def book_update(request, pk):
    book = get_object_or_404(Book, pk=pk, user=request.user)
    if request.method == "POST":
        form = BookForm(request.POST, instance=book)
        if form.is_valid():
            form.save()
            return redirect('book_list')
    else:
        form = BookForm(instance=book)
    return render(request, "books_app/book_form.html", {"form": form, "book": book})


# Delete a book
@login_required
def book_delete(request, pk):
    book = get_object_or_404(Book, pk=pk, user=request.user)
    if request.method == "POST":
        book.delete()
        return redirect('book_list')
    return render(request, 'books_app/book_confirm_delete.html', {'book': book})


# View book details and associated reviews
@login_required
def book_detail(request, pk):
    book = get_object_or_404(Book, pk=pk, user=request.user)
    reviews = book.reviews.all()

    if request.method == "POST":
        review_form = ReviewForm(request.POST)
        if review_form.is_valid():
            review = review_form.save(commit=False)
            review.book = book
            review.user = request.user
            review.save()
            return redirect('book_detail', pk=book.pk)
    else:
        review_form = ReviewForm()

    return render(request, 'books_app/book_detail.html', {
        'book': book,
        'reviews': reviews,
        'review_form': review_form
    })


# Update user's progress in a book
@login_required
def update_progress(request, pk):
    book = get_object_or_404(Book, pk=pk, user=request.user)

    if request.method == "POST":
        form = ProgressForm(request.POST, instance=book)
        if form.is_valid():
            form.save()
            return redirect('book_detail', pk=book.pk)
    else:
        form = ProgressForm(instance=book)

    return render(request, 'books_app/update_progress.html', {'form': form, 'book': book})


# Toggle a book as a favorite
@login_required
def toggle_favorite(request, pk):
    book = get_object_or_404(Book, pk=pk, user=request.user)
    book.favorite = not book.favorite
    book.save()
    return redirect('book_list')


# View all favorite books
@login_required
def favorite_books(request):
    books = Book.objects.filter(user=request.user, favorite=True)
    return render(request, 'books_app/favorite_books.html', {'books': books})
