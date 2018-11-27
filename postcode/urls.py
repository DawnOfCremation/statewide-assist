from django.contrib import admin
from django.urls import path

from .views import myView, faqPostCode, home

urlpatterns = [
    #path('', myView, name='postcode'),
    #path('', home, name='home'),#---->
    #path('', myView, name='myView'),
    path('myView/', myView, name='myview'),
    path('faqpostcode/', faqPostCode, name='faqpostcode'),


]
