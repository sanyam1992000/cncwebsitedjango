from django.db import models
from accounts.models import User, UserProfile


class SlideShowPic(models.Model):
    title = models.CharField(max_length=50, default=None)
    image = models.ImageField(default=None, upload_to='slide show pics')
    description = models.CharField(max_length=300)
    url = models.URLField(name='url')


class Member(models.Model):
    user = models.ForeignKey(UserProfile, on_delete=models.CASCADE)
    description = models.CharField(max_length=100)


class ContactUs(models.Model):
    name = models.CharField(max_length=50)
    email = models.EmailField(default=None)
    phoneno = models.BigIntegerField(default=None)
    query = models.TextField(max_length=2000)
