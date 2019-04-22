from django.contrib import admin
from django.urls import path
from .views import home, services, serviceGen, serviceBat, serviceJump, serviceFlat, serviceFuel, serviceLock, servicesMore


urlpatterns = [

    path('service/general_assist', serviceGen, name='serviceGen'),
    path('service/battery_assist', serviceBat, name='serviceBat'),
    path('service/battery_jump', serviceJump, name='serviceJump'),
    path('service/battery_flattyre', serviceFlat, name='serviceFlat'),
    path('service/battery_fuel', serviceFuel, name='serviceFuel'),
    path('service/battery_lockout', serviceLock, name='serviceLock'),
    path(r'^service/(?P<id>\d+)/$', servicesMore, name='servicesMore'),


]
