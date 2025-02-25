from django.contrib import admin
from django.urls import path, include
from django.contrib.auth import views as auth_views
from books_app.views import signup, custom_logout

urlpatterns = [
    path('admin/', admin.site.urls),
    path('books/', include('books_app.urls')),

    # Authentication URLs
    path('accounts/login/', auth_views.LoginView.as_view(), name='login'),
    path('accounts/logout/', custom_logout, name='logout'),  # Custom logout view
    path('accounts/signup/', signup, name='signup'),

    # Password Reset URLs (Fixing NoReverseMatch error)
    path('accounts/password_reset/', auth_views.PasswordResetView.as_view(), name='password_reset'),
    path('accounts/password_reset/done/', auth_views.PasswordResetDoneView.as_view(), name='password_reset_done'),
    path('accounts/reset/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(), name='password_reset_confirm'),
    path('accounts/reset/done/', auth_views.PasswordResetCompleteView.as_view(), name='password_reset_complete'),
    path('', RedirectView.as_view(url='books/', permanent=True)),
]
