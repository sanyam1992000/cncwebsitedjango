from django.core.mail import send_mail, EmailMessage
from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated, IsAdminUser
from .serializers import UserSerializer, UserProfileSerializer, BlogSerializer, EventSerializer
from accounts.models import UserProfile, FacultyProfile
from blog.models import Post
from events.models import Event
from .models import SlideShowPic, ContactUs, Member
from .forms import ContactUsForm
from django.contrib import messages
from django.conf import settings


def home(request):

    SlideShowPics = SlideShowPic.objects.all()
    upcomingevents = Event.objects.filter(status='True')
    events = Event.objects.filter(status='False')
    context = {
        'slideshows': SlideShowPics,
        'upcomingevents': upcomingevents,
        'events': events,
    }
    return render(request, 'home.html', context=context)


def about(request):
    members = Member.objects.all()
    faculties = FacultyProfile.objects.all()
    context = {
        'members': members,
        'faculties': faculties,

    }
    return render(request, 'core/about.html', context)


def contact_us(request):
    if request.method == 'POST':
        form = ContactUsForm(request.POST)
        if form.is_valid():
            name = request.POST['name']
            email = request.POST['email']
            phoneno = request.POST['phoneno']
            query = request.POST['query']
            contact_us = ContactUs(name=name, email=email, phoneno=phoneno, query=query)
            contact_us.save()

            subject = 'New Query on Website from {}'.format(name)
            message = '\n \n Career and Counselling Cell Website received a new query from {} \n \nMessage,\n' \
                      '     {} \n \nFrom: \n{} \nPhone no. - {}'.format(name, query, email, phoneno)
            from_email = settings.DEFAULT_FROM_EMAIL
            to_email = ['careerandcounsellingcell.ymca@gmail.com', ]
            send_mail(subject=subject, message=message, from_email=from_email, recipient_list=to_email, fail_silently=True)

            messages.success(request, 'We will Contact you soon!')
            return redirect('core:home')
        else:
            messages.error(request, 'invalid input')
    else:
        form = ContactUsForm()
    return render(request, 'contact us.html', {'form': form})


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