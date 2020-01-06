from django.contrib.auth.decorators import login_required
from django.core.mail import EmailMessage
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from .forms import UserRegistrationForm, UserLogin, EditUser, EditStudentProfile
from .models import UserProfile
from django.contrib.auth.models import User
from django.conf import settings
from events.views import Registration
from django.http import HttpResponseForbidden
# Create your views here.


def login_user(request):
    logout(request)
    if request.method == 'POST':
        form = UserLogin(request.POST)
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            redirect_url = request.GET.get('next', 'core:home')
            messages.success(request, 'You\'re logged in as Username: {}'.format(user.first_name))
            return redirect(redirect_url)
        else:
            messages.error(request, 'Username or Password is incorrect')
    else:
        form = UserLogin()
    return render(request, 'accounts/login1.html', {'form': form})


@login_required
def logout_user(request):
    logout(request)
    messages.info(request, 'Successfully Logged Out')
    return redirect('core:home')


def register(request):
    logout(request)
    if request.method == 'POST':
        form = UserRegistrationForm(request.POST, request.FILES)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password1']
            email = form.cleaned_data['email']
            roll_no = form.cleaned_data['roll_no']
            firstname = form.cleaned_data['first_name']
            lastname = form.cleaned_data['last_name']
            course = form.cleaned_data['course']
            branch = form.cleaned_data['branch']
            phoneno = form.cleaned_data['phoneno']
            icard = form.cleaned_data['icard']
            user = User.objects.create_user(username=username, email=email, password=password, first_name=firstname,
                                            last_name=lastname)
            # user.is_active = False
            user.save()
            profile = UserProfile(user=user, course=course, roll_no=roll_no, branch=branch, phoneno=phoneno, icard=icard)
            profile.save()

            ## for Sending email ##
            subject = 'Welcome to Career and Counseling Cell'
            message = user.first_name + ', thanks for registering on Career and Counseling Cell of ' \
                                      'JC BOSE UNIVERSITY OF SCIENCE AND TECHNOLOGY'
            from_email = settings.DEFAULT_FROM_EMAIL
            to_email = [email]
            email = EmailMessage(subject=subject, from_email=from_email, to=to_email, body=message)
            path = 'accounts/brochure.pdf'
            try:
                email.attach_file(path=path)
                email.send(fail_silently=True)
            except:
                email.send(fail_silently=True)
            #######

            messages.success(request, 'Thanks for registering {}'.format(user.first_name))
            return redirect('core:home')
        else:
            form = UserRegistrationForm(request.POST, request.FILES)
            messages.error(request, form.errors)
    else:
        form = UserRegistrationForm()
    return render(request, 'accounts/register1.html', {'form': form})


def ProfileDashboard(request, username):
    user = request.user
    user_instance = get_object_or_404(User, username=username)
    user_instance_profile = get_object_or_404(UserProfile, user=user_instance)
    registration = Registration.objects.filter(user=user_instance)
    context = {
        'user': user,
        'user_instance': user_instance,
        'certificates': registration,
        'profile': user_instance_profile,
    }
    return render(request, 'accounts/profile1.html', context)


@login_required
def EditStudentProfileView(request, username):
    user = request.user
    if user.username == username:
        if request.method == 'POST':

            userform = EditUser(request.POST, instance=user)
            studentform = EditStudentProfile(request.POST, request.FILES, instance=user.userprofile)

            if userform.is_valid() and studentform.is_valid():
                userform.save()
                studentform.save()
                messages.success(request, 'Your Profile is Updated')
                return redirect('core:home')
            else:
                form = UserRegistrationForm(request.POST, request.FILES)
                messages.error(request, form.errors)
        else:
            userform = EditUser(instance=user)
            studentform = EditStudentProfile(instance=user.userprofile)
        return render(request, 'accounts/edit_user_profile.html', {'userform': userform, 'studentform': studentform})
    else:
        return HttpResponseForbidden()

