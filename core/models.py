from django.db import models
from accounts.models import User, UserProfile
from django.shortcuts import get_object_or_404

member_description = (
    ('Student Co-ordinator', '1-Student Co-ordinator'),
    ('Member', '2-Member'),
    ('Ex Student Co-ordinator', '3-Ex Student Co-ordinator'),
    ('Ex Member', '4-Ex Member')
)

member_status = (
    ('Current', 'Current'),
    ('Alumni', 'Alumni'),
)


class SlideShowPic(models.Model):
    title = models.CharField(max_length=50, default=None, blank=True, null=True)
    image = models.ImageField(default=None, upload_to='slide show pics')
    description = models.CharField(max_length=300, blank=True, null=True)
    url = models.URLField(name='url')
    number = models.IntegerField(default=1, blank=True, null=True)

    def __str__(self):
        return self.title
    
    class Meta:
        ordering = ['number']


class Member(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    userprofile = models.ForeignKey(UserProfile, on_delete=models.CASCADE, default=None, blank=True, null=True)
    description = models.CharField(choices=member_description, max_length=100)
    status = models.CharField(choices=member_status, max_length=100, blank=True, null=True)

    def __str__(self):
        return str(self.user.username)

    def get_user_profile(self, user):
        userprofile1 = get_object_or_404(UserProfile, user=user)
        return userprofile1

    def save(self, *args, **kwargs):
        userprofile1 = self.get_user_profile(self.user)
        self.userprofile = userprofile1
        super().save(*args, **kwargs)  # call the actual save method

    class Meta:
        ordering = ['-description']


class ContactUs(models.Model):
    name = models.CharField(max_length=50)
    email = models.EmailField(default=None)
    phoneno = models.BigIntegerField(default=None)
    query = models.TextField(max_length=5000)

    def __str__(self):
        return str(self.name)


class Auditions(models.Model):
    name = models.CharField(max_length=1000)
    email = models.EmailField()
    phone = models.BigIntegerField()
    roll_no = models.BigIntegerField(blank=True, null=True)
    hobbies = models.TextField()
    skills = models.CharField(max_length=1000)
    course = models.CharField(max_length=1000)
    branch = models.CharField(max_length=1000)
    reason = models.TextField()
    ip = models.CharField(max_length=1000, default="NA", blank=True, null=True)
    browser = models.CharField(max_length=1000, default="NA", blank=True, null=True)

    def __str__(self):
        return str(self.name) + str(self.roll_no)
