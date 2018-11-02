from django.contrib import admin
from django.urls import path

from .views import emailView, successView#, emailTemp

urlpatterns = [
    path('email/', emailView, name='email'),
    path('success/', successView, name='success'),
    #path('emailtemp/', emailTemp, name='emailtemp'),
]
