from django.urls import path
from . import views


app_name = 'events'


urlpatterns = [
    path('', views.events, name='Events'),
    path('certi', views.getpdf, name='certi'),
    path('<userid>/<eventid>/', views.getpdf, name='certi'),
]
