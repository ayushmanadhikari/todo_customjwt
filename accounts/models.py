from django.db import models
from django.contrib.auth.models import AbstractUser
from rest_framework import serializers

# Create your models here.
class CustomUser(AbstractUser):
    username = models.CharField(max_length=50, blank=False, null=False, unique=True)
    email = models.EmailField(blank=True, null=True)
    name = models.CharField(max_length=100, blank=True, null=True)

    USERNAME_FIELD = 'username'

    def __str__(self):
        return self.username


# serializer for CustomUser model
class CustomUserSerializer(serializers.Serializer):
    class Meta:
        models = CustomUser
        fields = '__all__'