import os
from django.core.mail import send_mail, EmailMessage
from django.shortcuts import render


def home(request):
    # subject = 'SAMPLE MAIL'
    # message = 'creating first sample mail with attachment'
    # from_email = settings.DEFAULT_FROM_EMAIL
    # to_email = ['sanyam1992000@yopmail.com', ]
    # email = EmailMessage(subject=subject, from_email=from_email, to=to_email, body=message)
    # email.attach_file(path=path)
    # email.send(fail_silently=True)
    #send_mail(subject=subject, message=message, from_email=from_email, recipient_list=to_email, fail_silently=True)

    return render(request, 'home.html')


def about(request):
    return render(request, 'about.html')


def contact_us(request):
    return render(request, 'contact us.html')
