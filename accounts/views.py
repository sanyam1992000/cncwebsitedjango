from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from .forms import UserRegistrationForm, UserLogin
from .models import UserProfile
from django.contrib.auth.models import User
from . import forms
# Create your views here.


def login_user(request):
    if request.method == 'POST':
        form = UserLogin(request.POST)
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            redirect_url = request.GET.get('next', 'home')
            return redirect(redirect_url)
        else:
            messages.error(request, 'Username or password is incorrect')
    else:
        form = UserLogin()
    return render(request, 'accounts/login.html', {'form': form})


@login_required
def logout_user(request):
    logout(request)
    return redirect('')


def register(request):
    logout(request)
    if request.method == 'POST':
        form = UserRegistrationForm(request.POST)
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
            user = User.objects.create_user(username=username, email=email, password=password, first_name=firstname, last_name=lastname)
            user.is_active = False
            user.save()
            profile = UserProfile(user=user, course=course, roll_no=roll_no, branch=branch, phoneno=phoneno)
            profile.save()
            messages.success(request, 'Thanks for registering {}'.format(user.username))
            return HttpResponse('registration complete')
    else:
        form = UserRegistrationForm()
    return render(request, 'accounts/register.html', {'form': form})

