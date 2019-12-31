from django.shortcuts import render, get_object_or_404
from . import models
# Create your views here.python
from .models import Post, Comment


def blog(request):
    Posts = Post.objects.all()
    context = {
        'Posts': Posts,
        'Comment': Comment
    }
    return render(request, 'blog/blog.html', context=context)


def detail(request, postid):
    article = get_object_or_404(Post, id=int(postid))
    comments = article.comments.all()
    return render(request, "blog/detail.html", {"post": article, "comments": comments})
