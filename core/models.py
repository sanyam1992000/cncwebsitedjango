from django.db import models
from accounts.models import User, UserProfile
from django.shortcuts import get_object_or_404


class SlideShowPic(models.Model):
    title = models.CharField(max_length=50, default=None)
    image = models.ImageField(default=None, upload_to='slide show pics')
    description = models.CharField(max_length=300)
    url = models.URLField(name='url')

    def __str__(self):
        return self.title


class Member(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    userprofile = models.ForeignKey(UserProfile, on_delete=models.CASCADE, default=None, blank=True, null=True)
    description = models.CharField(max_length=100)

    def __str__(self):
        return str(self.user.username)

    def get_user_profile(self, user):
        userprofile1 = get_object_or_404(UserProfile, user=user)
        return userprofile1

    def save(self, *args, **kwargs):
        userprofile1 = self.get_user_profile(self.user)
        self.userprofile = userprofile1

        super().save(*args, **kwargs)  # call the actual save method


class ContactUs(models.Model):
    name = models.CharField(max_length=50)
    email = models.EmailField(default=None)
    phoneno = models.BigIntegerField(default=None)
    query = models.TextField(max_length=2000)
