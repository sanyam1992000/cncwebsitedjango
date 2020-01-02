from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from django.shortcuts import render, redirect, get_object_or_404
from .models import Event, Registration
from .certificates import render_to_pdf
from django.contrib.auth.models import User
# Create your views here.


def EventsList(request):
    events = Event.objects.all()
    context = {
        'events' : events
    }
    return render(request, 'events/eventlist.html', context)


def EventDetail(request, eventid):
    event = get_object_or_404(Event, id=eventid)
    context = {
        'event': event
    }
    return render(request, 'events/eventdetail.html', context)


#@login_required
def Getpdf(request, username, eventid, *args, **kwargs):
    user = User.objects.get(username=username)
    event = Event.objects.get(id=eventid)
    if username == user.username:
        data = {
            'user': user
        }
        pdf = render_to_pdf('events/certi1.html', )
        return HttpResponse(pdf, content_type='application/pdf')
    else:
        return render(request, '404.html')


@login_required
def RegisterForEvent(request, eventid):
    user = request.user
    event = Event.objects.filter(id=eventid)
    registration = Registration(user=user, event=event)
    registration.save()
    return redirect('events:EventsDetail')
