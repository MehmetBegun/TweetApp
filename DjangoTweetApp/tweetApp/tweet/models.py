from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Tweet(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    tweet = models.CharField(max_length=280)

    def __str__(self):
        return f"User: {self.user.username} Tweet: {self.tweet}"