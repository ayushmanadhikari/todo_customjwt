from django.db import models
from accounts.models import CustomUser
from rest_framework import serializers


# user defined custom category model for task category
class Category(models.Model):
    name = models.CharField(max_length=30)
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)

    def __str__(self):
        return self.name
    

# task model to define the overall task in the app
class Task(models.Model):
    status_choices= [
        ('NS', 'Not Started'), 
        ('OG', 'On Going'),
        ('F', 'Finished')
    ]

    name = models.CharField(max_length=200)
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True)
    status = models.CharField(max_length=20, choices=status_choices, default='NS')

    def __str__(self):
        return self.name


# category serializer
class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        models = Category
        fields = '__all__'


# task serializer
class TaskSerializer(serializers.ModelSerializer):
    class Meta:
        models = Task
        fields = '__all__'
    