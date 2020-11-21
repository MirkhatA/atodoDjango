from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse
from datetime import datetime, date
# Create your models here.

# email recieve


class Category(models.Model):
    name = models.CharField(max_length=255)
    author = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('home')


class Task(models.Model):
    title = models.CharField(max_length=255)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    body = models.TextField()
    completed = models.BooleanField(default=False)
    task_date = models.DateField()
    category = models.CharField(max_length=255, default='none')

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('home')
