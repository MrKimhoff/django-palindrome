# palindrome/urls.py

from django.urls import path
from .views import palindrome_view, clear_history

urlpatterns = [
    path('', palindrome_view, name='palindrome'),
    path('clear/', clear_history, name='clear_history'),
]