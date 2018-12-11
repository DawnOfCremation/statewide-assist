#postcode View File
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse
from django.shortcuts import render
from django.http import HttpResponse
from .models import Postcode
from .forms import PostcodeForm
from faq.models import Faq
from service.models import Service
import service.views
import faq.views

# Create your views here.
def home(request):#dont think this ones is being used
    mypostcode = Postcode.objects
    verdict = "!!Add your current breakdown location's post code below to check if the area is covered by us."
    return render(request, 'home.html', {'verdict': verdict})


def myView(request):
    services = Service.objects
    #fulltext = request.GET['fulltext']
    mypostcode = Postcode.objects
    verdict = "Enter your post code below to check if the area is covered by us."
    #PostCodeList = []

    #for i in Postcode.objects.all():
    #    postcodeStr = i.postcode
    #    PostCodeList.append(postcodeStr)

    #if fulltext in PostCodeList:
    #    verdict = "Yes you are covered, call us now on 0488 602 271"
    #else:
    #    verdict = "Sorry your area is not covered!"

    #print(PostCodeList)
    #if request.method == 'POST' and 'input' in request.POST:
    return render(request, 'home.html',{'services':services,'verdict': verdict})



def faqPostCode(request):
    faqs = Faq.objects
    services = Service.objects
    #fulltext = request.GET['fulltext']
    #mypostcode = Postcode.objects
    verdict = "Enter your post code below to check if the area is covered by us."
    #PostCodeList = []

    #for i in Postcode.objects.all():
    #    postcodeStr = i.postcode
    #    PostCodeList.append(postcodeStr)

    #if fulltext in PostCodeList:
    #    verdict = "Yes you are covered, call us now on 0488 602 271"
    #else:
    #    verdict = "Sorry your area is not covered!"

    #print(PostCodeList)
    #if request.method == 'POST' and 'input' in request.POST:
    return render(request, 'faq.html',{'faqs':faqs, 'services':services,'verdict': verdict})


#@csrf_exempt
def postCodeCheck(request):
    #if request.method == 'GET':
    if request.is_ajax():
        code = request.GET['checkpost']
        print('my entered code - ' + code)
        PostCodeList = []

        for i in Postcode.objects.all():
            postcodeStr = i.postcode
            PostCodeList.append(postcodeStr)

        if code in PostCodeList:
            #return HttpResponse('')
            return HttpResponse('We cover your location please call 0488 602 271 for assistance')
            print('Yes indeed')

        else:
            return HttpResponse("Unfortunately we don't cover that area")
            print('Nope not working')
