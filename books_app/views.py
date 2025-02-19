from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from .models import Book, Review
from .forms import BookForm, ReviewForm

@login_required
def book_list(request):
    """View to list all books belonging to the logged-in user."""
    books = Book.objects.filter(user=request.user)
    return render(request, 'books_app/book_list.html', {'books': books})

@login_required
def book_create(request):
    """View to add a new book."""
    if request.method == "POST":
        form = BookForm(request.POST)
        if form.is_valid():
            book = form.save(commit=False)
            book.user = request.user
            book.save()
            return redirect('book_list')
    else:
        form = BookForm()
    return render(request, 'books_app/book_form.html', {'form': form})

@login_required
def book_update(request, pk):
    """View to update a book's details."""
    book = get_object_or_404(Book, pk=pk, user=request.user)
    if request.method == "POST":
        form = BookForm(request.POST, instance=book)
        if form.is_valid():
            form.save()
            return redirect('book_list')
    else:
        form = BookForm(instance=book)
    return render(request, 'books_app/book_form.html', {'form': form})

@login_required
def book_delete(request, pk):
    """View to delete a book."""
    book = get_object_or_404(Book, pk=pk, user=request.user)
    if request.method == "POST":
        book.delete()
        return redirect('book_list')
    return render(request, 'books_app/book_confirm_delete.html', {'book': book})

@login_required
def book_detail(request, pk):
    """View to show book details and reviews."""
    book = get_object_or_404(Book, pk=pk, user=request.user)
    reviews = book.reviews.all()
    if request.method == "POST":
        form = ReviewForm(request.POST)
        if form.is_valid():
            review = form.save(commit=False)
            review.book = book
            review.user = request.user
            review.save()
            return redirect('book_detail', pk=book.pk)
    else:
        form = ReviewForm()
    return render(request, 'books_app/book_detail.html', {'book': book, 'reviews': reviews, 'form': form})

@login_required
def update_progress(request, pk):
    """View to update the user's progress in a book."""
    book = get_object_or_404(Book, pk=pk, user=request.user)
    if request.method == "POST":
        new_page = int(request.POST.get("current_page", 0))
        if 0 <= new_page <= book.total_pages:
            book.current_page = new_page
            book.save()
    return redirect('book_detail', pk=book.pk)

@login_required
def toggle_favorite(request, pk):
    """View to toggle a book as a favorite."""
    book = get_object_or_404(Book, pk=pk, user=request.user)
    book.favorite = not book.favorite
    book.save()
    return redirect('book_list')

@login_required
def favorite_books(request):
    """View to show all favorite books."""
    books = Book.objects.filter(user=request.user, favorite=True)
    return render(request, 'books_app/favorite_books.html', {'books': books})
