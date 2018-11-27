from django.shortcuts import render
from postcode.models import Postcode
from service.models import Service

from .models import Faq

def faq(request):
    faqs = Faq.objects
    services = Service.objects
    mypostcode = Postcode.objects
    verdict = "Add your current breakdown location's post code below to check if the area is covered by us!!."
    return render(request, 'faq.html', {'faqs':faqs, 'services':services, 'verdict': verdict})
