from django.db import models

# Create your models here.
class PalindromeEntry(models.Model):
    text = models.CharField(max_length=255)
    is_palindrome = models.BooleanField()
    timestamp = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return f"{self.text} - {'✅' if self.is_palindrome else '❌'}"