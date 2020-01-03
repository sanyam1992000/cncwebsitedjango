from django.urls import path,include
from . import views


app_name = 'blog'


urlpatterns = [
    path('', views.blog, name='blog'),
    path('<postid>/', views.detail, name='detail'),
    path('<postid>/<commentid>/', views.CommentDelete, name='comment_delete')
]
