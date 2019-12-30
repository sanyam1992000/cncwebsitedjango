from django.db import models
from django.contrib.auth import authenticate, login, logout

# Create your models here.
from django.db.models import CharField


class Post(models.Model):
    title = models.CharField(max_length=100)
    description = models.CharField(max_length=500)
    content = models.TextField(max_length=100)
    date = models.DateTimeField(auto_now=True)
    pic1 = models.ImageField(default=None, upload_to='blog pics')
    pic2 = models.ImageField(default=None, upload_to='blog pics')
    pic3 = models.ImageField(default=None, upload_to='blog pics')
    pic4 = models.ImageField(default=None, upload_to='blog pics')
    pic5 = models.ImageField(default=None, upload_to='blog pics')

    def __str__(self):
        return self.title

    class Meta:
        ordering = ['-date']


class Comment(models.Model):
    article = models.ForeignKey(Post, on_delete=models.CASCADE, related_name="comments")
    comment_author = models.CharField(max_length=50)
    comment_content = models.CharField(max_length=200)
    comment_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.comment_content

    class Meta:
        ordering = ['-comment_date']
