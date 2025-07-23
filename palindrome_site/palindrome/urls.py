# palindrome/urls.py

from django.urls import path
from .views import check_palindrome_view, clear_history

urlpatterns = [
    path('', check_palindrome_view, name='palindrome'),
    path('clear/', clear_history, name='clear_history'),
]