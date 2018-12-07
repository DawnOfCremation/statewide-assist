#service View File
from django.shortcuts import render
from .models import Service
from postcode.models import Postcode
#from postcode.views import myView
import postcode.views
from django.conf import settings


def home(request):
    services = Service.objects
    mypostcode = Postcode.objects
    verdict = "Add your current breakdown location's post code below to check if the area is covered by us!!."
    mapbox_access_token = settings.MAPBOX_MAP_ID
    print (type(mapbox_access_token))
    return render(request, 'home.html', {'services':services, 'verdict': verdict, 'mapbox_access_token': mapbox_access_token })

def servicesMore(request, id):
    services = Service.objects
    myid = int(id)
    return render(request, 'service.html', {'services':services, 'myid':myid})


def services(request):
    services = Service.objects
    return render(request, 'services.html', {'services':services})

def serviceGen(request):
    services = Service.objects
    myid = 1
    return render(request, 'service.html', {'services':services, 'myid':myid})

def serviceBat(request):
    services = Service.objects
    myid = 2
    return render(request, 'service.html', {'services':services, 'myid':myid})


def serviceJump(request):
    services = Service.objects
    myid = 3
    return render(request, 'service.html', {'services':services, 'myid':myid})


def serviceFlat(request):
    services = Service.objects
    myid = 4
    return render(request, 'service.html', {'services':services, 'myid':myid})


def serviceFuel(request):
    services = Service.objects
    myid = 5
    return render(request, 'service.html', {'services':services, 'myid':myid})

def serviceLock(request):
    services = Service.objects
    myid = 6
    return render(request, 'service.html', {'services':services, 'myid':myid})
