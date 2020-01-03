from django.db import models
from accounts.models import User, UserProfile


class SlideShowPic(models.Model):
    image = models.ImageField(default=None, upload_to='slide show pics')
    description = models.CharField(max_length=300)
    url = models.URLField(name='url')


class Member(models.Model):
    user = models.ForeignKey(UserProfile, on_delete=models.CASCADE)
    description = models.CharField(max_length=100)

