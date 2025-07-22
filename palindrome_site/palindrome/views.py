# palindrome/views.py

from django.shortcuts import render, redirect
from .models import PalindromeEntry
from .utils import is_palindrome
from django.views.decorators.http import require_POST

# Create your views here.
def palindrome_view(request):
    if request.method == 'POST':
        text = request.POST.get('text', '')
        result = is_palindrome(text)
        PalindromeEntry.objects.create(text=text, is_palindrome=result)
        return redirect('palindrome') # clear form and reload history
    
    history = PalindromeEntry.objects.order_by('-timestamp')[:20]
    return render(request, 'palindrome/index.html', {
        'history': history
    })
    
@require_POST
def clear_history(request):
    PalindromeEntry.objects.all().delete()
    return redirect('palindrome')
    