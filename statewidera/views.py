from django.http import HttpResponse
from django.shortcuts import render
from django.core.mail import send_mail
from django.conf import settings


def home(request):
    return render(request, 'home.html', {'hithere': 'This is me'})


def about(request):
    return render(request, 'about.html', {'aboutme': 'Lets Count!'})


def contact(request):
        return render(request, 'contact.html')
