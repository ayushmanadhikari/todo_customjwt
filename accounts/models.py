from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.
class CustomUser(AbstractUser):
    username = models.CharField(max_length=50, blank=False, null=False, unique=True)
    email = models.EmailField(blank=True, null=True)
    name = models.CharField(blank=True, null=True)

    REQUIRED_FIELDS = ['username']
    USERNAME_FIELD = 'username'
    
    def __str__(self):
        return self.username