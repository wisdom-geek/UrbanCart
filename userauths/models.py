from django.contrib.auth.models import AbstractUser
from django.db import models

class User(AbstractUser):
    email = models.EmailField(unique=True)
    username = models.CharField(max_length=100)
    bio = models.CharField(max_length=100, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)  
    
    USERNAME_FIELD = 'email'  # Use email as the unique identifier
    REQUIRED_FIELDS = ['username']  # Additional fields required for createsuperuser command
    
    class Meta:
        ordering = ['created_at']

    def __str__(self):
        return self.username