from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from .models import Book, Review
from .forms import BookForm, ReviewForm, ProgressForm

"""View to list all books belonging to the logged-in user."""
@login_required
def book_list(request):
    books = Book.objects.filter(user=request.user)
    return render(request, 'books_app/book_list.html', {'books': books})


"""View to add a new book."""
@login_required
def book_create(request):
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


"""View to update a book's details."""
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


"""View to delete a book."""
@login_required
def book_delete(request, pk):
    book = get_object_or_404(Book, pk=pk, user=request.user)
    if request.method == "POST":
        book.delete()
        return redirect('book_list')
    return render(request, 'books_app/book_confirm_delete.html', {'book': book})


"""View to show book details and reviews."""
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


"""View to update the user's progress in a book."""
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


"""View to toggle a book as a favorite."""
@login_required
def toggle_favorite(request, pk):
    book = get_object_or_404(Book, pk=pk, user=request.user)
    book.favorite = not book.favorite
    book.save()
    return redirect('book_list')


"""View to show all favorite books."""
@login_required
def favorite_books(request):
    books = Book.objects.filter(user=request.user, favorite=True)
    return render(request, 'books_app/favorite_books.html', {'books': books})
