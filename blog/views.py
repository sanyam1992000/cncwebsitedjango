from django.core.paginator import Paginator
from django.shortcuts import render, get_object_or_404, redirect
import datetime
from . import models
from .forms import CommentForm
from .models import Post, Comment


def blog(request):
    post_all = Post.objects.all().order_by('-date')
    paginator_post = Paginator(post_all, 5)
    page = request.GET.get('page')
    posts = paginator_post.get_page(page)
    context = {
        'allposts': paginator_post,
        'posts': posts,
    }
    return render(request, 'blog/blog_list.html', context=context)


def detail(request, postid):
    article = get_object_or_404(Post, id=int(postid))
    comments = article.comments.all()
    user = request.user
    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.cleaned_data['comment_content']
            date = datetime.datetime.now()
            comment = Comment(comment_content=comment, comment_user=user, article=article, comment_date=date)
            comment.save()
            form = CommentForm()
    else:
        form = CommentForm()

    return render(request, "blog/detail.html", {"post": article, "comments": comments, 'form': form})


def CommentDelete(request, postid, commentid):
    comment = models.Comment.objects.get(id=commentid)
    comment.delete()

    return redirect('blog:detail', postid)
