from django.http import HttpResponse
from django.shortcuts import render


def home(request):
    return render(request, 'home.html', {'hithere': 'This is me'})



def about(request):
    return render(request, 'about.html', {'aboutme': 'Lets Count!'})


def gethelp(request):
    return render(request, 'callassistance.html' {'help': 'help me!'})
