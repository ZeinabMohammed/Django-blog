from django.contrib import admin
from django.urls import path,include
from .views import *
from django.contrib.auth.views import LoginView, LogoutView, PasswordResetView, PasswordResetDoneView, PasswordResetConfirmView
app_name="users"


urlpatterns = [
    path('register/', register, name='register'),
    path('login/', LoginView.as_view(template_name='users/login.html') , name='login'),
    path('logout/', LogoutView.as_view(template_name='users/logout.html') , name='logout'),
    path('password-reset/', PasswordResetView.as_view(template_name='users/password_reset.html') , name='password_reset'),
    # path('password-reset/done', PasswordResetDoneView.as_view(template_name='users/password_reset_done.html') , name='password_reset_done'),
    # path('password-reset-confirm/<uidb64>/<token>/', PasswordResetConfirmView.as_view(template_name='users/password_reset_confirm.html') , name='password_reset_confirm'),
    path('', include('registration.backends.default.urls')),
    path('profile/', profile , name='profile'),
    # path('about/', about, name='about'),
]