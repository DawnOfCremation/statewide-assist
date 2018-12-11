from django.contrib import admin
from django.urls import path

from django.contrib.staticfiles.urls import staticfiles_urlpatterns

from .views import myView, faqPostCode, home, postCodeCheck


urlpatterns = [

    #path('', myView, name='postcode'),
    #path('', home, name='home'),#---->
    #path('', myView, name='myView'),
    #path('myView/', myView, name='myview'),
    path('faqpostcode/', faqPostCode, name='faqpostcode'),
    path('postcodecheck/', postCodeCheck, name='postcodecheck')


]
