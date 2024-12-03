from django.core.mail import send_mail, BadHeaderError
from django.shortcuts import render, HttpResponse


def sending_mail(request):
    try:
        send_mail(subject='subject', message='message', html_message='<p>Hello World!</p>', from_email='info@nasiri.me', recipient_list=[
            'bob@domain.com'])
    except BadHeaderError:
        print('Bad')
    return HttpResponse('ok')
