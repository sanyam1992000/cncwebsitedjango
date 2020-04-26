from django.core.paginator import Paginator
from django.shortcuts import render, get_object_or_404, redirect
import datetime
from . import models
from .forms import CommentForm
from .models import Post, Comment


def blog(request):
    post_all = Post.objects.all().order_by('-date')
    get_dict_copy = request.GET.copy()
    
    search_term = ''
    
    if 'month' and 'year' and 'search' in request.GET:
        m = request.GET['month']
        y = request.GET['year']
        search_term = request.GET['search']
        
        if m == '' and y == '':
            post_all = Post.objects.filter(title__icontains=search_term).order_by('-date')
        elif m == '':
            y = int(y)
            post_all = Post.objects.filter(date__year=y, title__icontains=search_term).order_by('-date')
        elif y=='':
            m = int(m)
            post_all = Post.objects.filter(date__month=m, title__icontains=search_term).order_by('-date')

        else:
            m = int(m)
            y = int(y)
            post_all = Post.objects.filter(date__gte=datetime.date(y, m, 1), date__lt=datetime.date(y, m+1, 1), title__icontains=search_term).order_by('-date')
    
    paginator_post = Paginator(post_all, 13)
    page = request.GET.get('page')
    posts = paginator_post.get_page(page)
    params = get_dict_copy.pop('page', True) and get_dict_copy.urlencode()

    context = {
        'allposts': paginator_post,
        'posts': posts,
        'params': params,
        'search_term': search_term,
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
