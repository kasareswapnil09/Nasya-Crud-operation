# app_name/models.py

from django.db import models
from django.contrib.auth.models import User

class Statistic(models.Model):
    title = models.CharField(max_length=100)
    value = models.IntegerField()

    def __str__(self):
        return self.title

class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    # Add fields for user profile, e.g., profile picture, additional information

    def __str__(self):
        return self.user.username
