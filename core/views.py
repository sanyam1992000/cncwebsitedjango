from django.core.mail import send_mail, EmailMessage
from django.shortcuts import render
from django.contrib.auth.models import User
from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated, IsAdminUser
from .serializers import UserSerializer, UserProfileSerializer, BlogSerializer, EventSerializer
from accounts.models import UserProfile
from blog.models import Post
from events.models import Event


def home(request):
    # subject = 'SAMPLE MAIL'
    # message = 'creating first sample mail with attachment'
    # from_email = settings.DEFAULT_FROM_EMAIL
    # to_email = ['sanyam1992000@yopmail.com', ]
    # email = EmailMessage(subject=subject, from_email=from_email, to=to_email, body=message)
    # email.attach_file(path=path)
    # email.send(fail_silently=True)
    # send_mail(subject=subject, message=message, from_email=from_email, recipient_list=to_email, fail_silently=True)

    return render(request, 'home.html')


def about(request):
    return render(request, 'about.html')


def contact_us(request):
    return render(request, 'contact us.html')


##### API VIEWS


class UserViewSet(viewsets.ModelViewSet):
    serializer_class = UserSerializer
    queryset = User.objects.all()

    def get_permissions(self):
        permission_classes = [IsAdminUser, ]
        return [permission() for permission in permission_classes]


class UserProfileViewSet(viewsets.ModelViewSet):
    serializer_class = UserProfileSerializer
    queryset = UserProfile.objects.all()

    def get_permissions(self):
        permission_classes = [IsAdminUser, ]
        return [permission() for permission in permission_classes]


class BlogViewSet(viewsets.ModelViewSet):
    serializer_class = BlogSerializer
    queryset = Post.objects.all()

    def get_permissions(self):
        permission_classes = [IsAdminUser, ]
        return [permission() for permission in permission_classes]


class EventViewSet(viewsets.ModelViewSet):
    serializer_class = EventSerializer
    queryset = Event.objects.all()

    def get_permissions(self):
        permission_classes = [IsAdminUser, ]
        return [permission() for permission in permission_classes]