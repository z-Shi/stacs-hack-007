from django.db import models
from django.contrib.auth.models import User


class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    points = models.IntegerField(default=0)
    controller = models.BooleanField(default=False)
    website = models.URLField(blank=True)
    picture = models.ImageField(upload_to='profile_images', blank=True)

    def __str__(self):
        return self.user.username


class Mission(models.Model):
    title = models.TextField(max_length=50)
    brief = models.TextField(max_length=200)
    points = models.IntegerField(default=5)

    def __str__(self):
        return self.title
