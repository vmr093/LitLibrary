from django.urls import path
from . import views

urlpatterns = [
    path('', views.book_list, name='book_list'),
    path('create/', views.book_create, name='book_create'),
    path('<int:pk>/update/', views.book_update, name='book_update'),
    path('<int:pk>/delete/', views.book_delete, name='book_delete'),
    path('<int:pk>/', views.book_detail, name='book_detail'),
    path('<int:pk>/update-progress/', views.update_progress, name='update_progress'),
    path('<int:pk>/toggle-favorite/', views.toggle_favorite, name='toggle_favorite'),
    path('favorites/', views.favorite_books, name='favorite_books'),
]
