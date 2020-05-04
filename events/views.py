from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from django.shortcuts import render, redirect, get_object_or_404
from .models import Event, Registration
from accounts.models import UserProfile
from .certificates import render_to_pdf, render_pdf_view
from django.contrib.auth.models import User
import datetime
from django.contrib import messages
from django.core.paginator import Paginator
import urllib.request


# Create your views here.


def EventsList(request):
    events = Event.objects.filter(status='False').order_by('-date')
    get_dict_copy = request.GET.copy()

    search_term = ''
    if 'month' and 'year' and 'search' in request.GET:
        m = request.GET['month']
        y = request.GET['year']
        search_term = request.GET['search']

        if m == '' and y == '':
            events = Event.objects.filter(status='False',event_name__icontains=search_term).order_by('-date')
        elif m == '':
            y = int(y)
            events = Event.objects.filter(status='False', date__year=y, event_name__icontains=search_term).order_by('-date')
        elif y=='':
            m = int(m)
            events = Event.objects.filter(status='False', date__month=m, event_name__icontains=search_term).order_by('-date')

        else:
            m = int(m)
            y = int(y)
            events = Event.objects.filter(status='False', date__gte=datetime.date(y, m, 1), date__lt=datetime.date(y, m+1, 1), event_name__icontains=search_term).order_by('-date')

    elif 'search' in request.GET:
        search_term = request.GET['search']
        events = Event.objects.filter(status='False', event_name__icontains=search_term).order_by('-date')

    paginator_event = Paginator(events, 10)
    page = request.GET.get('page')
    events = paginator_event.get_page(page)

    params = get_dict_copy.pop('page', True) and get_dict_copy.urlencode()
    context = {
        'allevents': paginator_event,
        'events': events,
        'params': params,
        'search_term': search_term,
    }
    return render(request, 'events/event_list.html', context)


def EventDetail(request, eventid):
    event = get_object_or_404(Event, id=eventid)
    user = request.user
    try:
        registration = Registration.objects.get(user=user, event=event)
    except:
        registration = None

    context = {
        'event': event,
        'registration': registration
    }
    return render(request, 'events/event_detail1.html', context)


def Getpdf(request, username, eventid, *args, **kwargs):
    user = get_object_or_404(User, username=username)
    event = get_object_or_404(Event, id=eventid)
    userprofile = get_object_or_404(UserProfile, user=user)
    if username == user.username:
        data = {
            'user': user,
            'event': event,
            'userprofile': userprofile,
        }
        return render(request, 'events/certi.html', data)
        # pdf = render_pdf_view(request, 'events/certi.html', data)
        # return HttpResponse(pdf, content_type='application/pdf')
    else:
        return HttpResponse('404')


@login_required
def RegisterForEvent(request, eventid):
    user = request.user
    event = get_object_or_404(Event, id=eventid)
    registration = Registration.objects.get_or_create(user=user, event=event)
    messages.success(request, 'Thanks for registering for Event - {}'.format(event.event_name))
    return redirect('events:events_detail', eventid=event.id)


@login_required
def UnregisterForEvent(request, eventid):
    user = request.user
    event = get_object_or_404(Event, id=eventid)
    registration = get_object_or_404(Registration, user=user, event=event)
    registration.delete()
    messages.error(request, 'You\'ve Unregistered for Event - {}'.format(event.event_name))
    return redirect('events:events_detail', eventid=event.id)
