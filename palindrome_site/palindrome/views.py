# palindrome/views.py

from django.shortcuts import render, redirect
from .models import PalindromeEntry
from .utils import is_palindrome
from django.views.decorators.http import require_POST

# Create your views here.
def check_palindrome_view(request):
    entry = None
    text = ""
    result = None
    
    if request.method == 'POST':
        text = request.POST.get('text', '')
        result = is_palindrome(text)
        
        entry, created = PalindromeEntry.objects.get_or_create(
            text=text,
            defaults={'is_palindrome': result}

        )
        
        print('made it here')
        
    # get 10 most recent historical entries
    history = PalindromeEntry.objects.order_by('-timestamp')[:10]
    
    return render(request, 'palindrome/index.html', {
        'entry': entry,
        'text': text,
        'history': history,
        'result': result,
    })
    
@require_POST
def clear_history(request):
    PalindromeEntry.objects.all().delete()
    return redirect('palindrome')