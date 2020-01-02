from django import forms
from .models import Comment
from django.core.exceptions import ValidationError
from django.contrib.auth.models import User


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('comment_content',)
