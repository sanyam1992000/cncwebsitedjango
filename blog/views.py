from django.shortcuts import render

# Create your views here.python


def blog(request):
    return render(request, 'blog/blog.html')
