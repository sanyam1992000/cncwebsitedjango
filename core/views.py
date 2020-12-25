from django.core.mail import send_mail, EmailMessage
from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from rest_framework import viewsets, authentication
from rest_framework.permissions import IsAuthenticated, IsAdminUser
from .serializers import UserSerializer, UserProfileSerializer, BlogSerializer, EventSerializer
from accounts.models import UserProfile, FacultyProfile
from blog.models import Post
from events.models import Event
from .models import SlideShowPic, ContactUs, Member, Auditions
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

def auditions(request):
    if request.method == 'POST':
        name = request.POST['name']
        email = request.POST['email']
        rollno = request.POST['rollno']
        phoneno = request.POST['phoneno']
        hobbies = request.POST['hobbies']
        skills = request.POST['skills']
        course = request.POST['course']
        branch = request.POST['branch']
        reason = request.POST['reason']

        try:
            audition = Auditions.objects.create(name=name, email=email, phone=phoneno, hobbies=hobbies, skills=skills, course=course, branch=branch, reason=reason)
            if rollno:
                audition.roll_no = rollno
                audition.save()
            subject = 'Thanks for Registering, {}'.format(name)
            message = 'Dear {}, \nThanks for registering for Auditions 2020. Please Join Whatsapp group for more info https://chat.whatsapp.com/KO0Ri1ZDyIg7PRvN0WMi66 \n\nRegards, \nCareer and Counselling Cell'.format(name)
            from_email = settings.DEFAULT_FROM_EMAIL
            to_email = [email,]
            send_mail(subject=subject, message=message, from_email=from_email, recipient_list=to_email, fail_silently=True)

            messages.success(request, 'Please Join Whatsapp Group - https://chat.whatsapp.com/KO0Ri1ZDyIg7PRvN0WMi66')
            return redirect('core:home')
        except Exception as err:
            messages.success(request, 'Something went wrong please register again')
            return render(request, 'auditions/auditions2020.html')
    else:
        return render(request, 'auditions/auditions2020.html')

def analyst(request):
    return render(request, 'quiz/analyst.html')

def avtar(request):
    return render(request, 'quiz/avtar.html')

def currentaffairs(request):
    return render(request, 'quiz/currentaffair.html')

def dribble(request):
    return render(request, 'quiz/dribble.html')

def musketeer(request):
    return render(request, 'quiz/musketeer.html')

def rabindernath(request):
    return render(request, 'quiz/rabindernath.html')


def silentpast(request):
    return render(request, 'quiz/silentpast.html')


def snapes_in_plane(request):
    return render(request, 'quiz/snapes-in-plane.html')


def therohanchaudharyshow(request):
    return render(request, 'quiz/therohanchaudharyshow.html')


def treasurer(request):
    return render(request, 'quiz/treasurer.html')


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
    authentication_classes = (authentication.TokenAuthentication,)


    def get_permissions(self):
        permission_classes = [IsAdminUser, ]
        return [permission() for permission in permission_classes]


class UserProfileViewSet(viewsets.ModelViewSet):
    serializer_class = UserProfileSerializer
    queryset = UserProfile.objects.all()
    authentication_classes = (authentication.TokenAuthentication,)

    def get_permissions(self):
        permission_classes = [IsAdminUser, ]
        return [permission() for permission in permission_classes]


class BlogViewSet(viewsets.ModelViewSet):
    serializer_class = BlogSerializer
    queryset = Post.objects.all()
    authentication_classes = (authentication.TokenAuthentication,)

    def get_permissions(self):
        permission_classes = [IsAdminUser, ]
        return [permission() for permission in permission_classes]


class EventViewSet(viewsets.ModelViewSet):
    serializer_class = EventSerializer
    queryset = Event.objects.all()
    authentication_classes = (authentication.TokenAuthentication,)

    def get_permissions(self):
        permission_classes = [IsAdminUser, ]
        return [permission() for permission in permission_classes]


def handler404(request, exception):
    return render(request, '404.html', status=404)


def handler500(request):
    return render(request, '500.html', status=500)


def handler403(request,exception):
    return render(request, '403.html', status=403)


def handler400(request,exception):
    return render(request, '400.html', status=400)