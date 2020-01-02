from django.core.paginator import Paginator
from django.shortcuts import render, get_object_or_404
from . import models
from .forms import CommentForm
# Create your views here.python
from .models import Post, Comment


def blog(request):
    post_all = Post.objects.all()
    paginator_post = Paginator(post_all, 1)
    page = request.GET.get('page')
    posts = paginator_post.get_page(page)
    context = {
        'allposts': paginator_post,
        'posts': posts,
        'Comment': Comment
    }
    return render(request, 'blog/blogs1.html', context=context)


def detail(request, postid):
    article = get_object_or_404(Post, id=int(postid))
    comments = article.comments.all()
    user = request.user
    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.cleaned_data['comment_content']
            comment = Comment(comment_content=comment, comment_user=user, article=article)
    else:
        form = CommentForm()

    return render(request, "blog/detail.html", {"post": article, "comments": comments, 'form':form})
