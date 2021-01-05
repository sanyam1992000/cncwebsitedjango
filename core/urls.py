from django.conf import settings
from django.conf.urls.static import static
from django.urls import path, include
from .views import home, about, contact_us, UserViewSet, UserProfileViewSet, BlogViewSet, EventViewSet, auditions
from . import views as coreviews
from rest_framework.routers import DefaultRouter
app_name = 'core'

router = DefaultRouter()
router.register('users', UserViewSet, basename='user')
router.register('userprofiles', UserProfileViewSet, basename='userprofile')
router.register('blogs', BlogViewSet, basename='blog')
router.register('events', EventViewSet, basename='event')


urlpatterns = [
    path('', home, name='home'),
    # path('auditions/', auditions, name='auditions'),

    path('analyst/', coreviews.analyst),
    path('avtar/', coreviews.avtar),
    path('current-affairs/', coreviews.currentaffairs),
    path('dribble/', coreviews.dribble),
    path('musketeer/', coreviews.musketeer),
    path('rabindranath/', coreviews.rabindernath),
    path('silent-past/', coreviews.silentpast),
    path('snapes-in-plane/', coreviews.snapes_in_plane),
    path('the-rohan-chaudhary-show/', coreviews.therohanchaudharyshow),
    path('treasurer/', coreviews.treasurer),


    path('about/', about, name='about'),
    path('contact/', contact_us, name='contact'),

    path('api/', include(router.urls)),

]

