from django.conf import settings
from django.conf.urls.static import static
from django.urls import path, include
from .views import home, about, contact_us, UserViewSet, UserProfileViewSet, BlogViewSet, EventViewSet
from rest_framework.routers import DefaultRouter
app_name = 'core'

router = DefaultRouter()
router.register('users', UserViewSet, basename='user')
router.register('userprofiles', UserProfileViewSet, basename='userprofile')
router.register('blogs', BlogViewSet, basename='blog')
router.register('events', EventViewSet, basename='event')


urlpatterns = [
    path('', home, name='home'),

    path('about/', about, name='about'),
    path('contact/', contact_us, name='contact'),

    path('api/', include(router.urls)),

]

