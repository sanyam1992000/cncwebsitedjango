from django.urls import path
from . import views


app_name = 'events'


urlpatterns = [
    path('', views.EventsList, name='events_list'),
    path('<int:eventid>/', views.EventDetail, name='events_detail'),
    path('certi', views.Getpdf, name='certi'),
    path('<username>/<eventid>/', views.Getpdf, name='certificate'),
    path('<eventid>/register', views.RegisterForEvent, name='register_for_event')

]
