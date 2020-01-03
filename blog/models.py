from django.contrib.auth.models import User
from django.db import models
# Create your models here.


class Post(models.Model):
    title = models.CharField(max_length=100)
    description = models.CharField(max_length=500)
    content = models.TextField()
    date = models.DateTimeField(auto_now_add=False, editable=True)
    pic1 = models.ImageField(default=None, upload_to='blog pics', blank=True, null=True)
    pic2 = models.ImageField(default=None, upload_to='blog pics', blank=True, null=True)
    pic3 = models.ImageField(default=None, upload_to='blog pics', blank=True, null=True)
    pic4 = models.ImageField(default=None, upload_to='blog pics', blank=True, null=True)
    pic5 = models.ImageField(default=None, upload_to='blog pics', blank=True, null=True)

    def __str__(self):
        return self.title

    class Meta:
        ordering = ['-date']


class Comment(models.Model):
    article = models.ForeignKey(Post, on_delete=models.CASCADE, related_name="comments")
    comment_user = models.ForeignKey(User, on_delete=models.CASCADE)
    comment_content = models.CharField(max_length=200)
    comment_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.comment_content

    class Meta:
        ordering = ['-comment_date']
