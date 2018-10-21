from django.http import HttpResponse
from django.shortcuts import render


def home(request):
    return render(request, 'home.html', {'hithere': 'This is me'})

def home2(request):
    return render(request, 'home2.html')

def home3(request):
    return render(request, 'home3.html')



def about(request):
    return render(request, 'about.html', {'aboutme': 'Lets Count!'})


def assistance(request):
    return render(request, 'callassistance.html')
