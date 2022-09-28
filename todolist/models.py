from statistics import mode
from turtle import title
from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class task(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    date = models.DateField(auto_now=True)
    title = models.CharField(max_length=100)
    description = models.TextField()