
#from django.conf.urls import url
from django.contrib import admin
from django.urls import path, include
from . import views


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home, name='home'),
    path('home2/', views.home2, name='home2'),
    path('home3/', views.home3, name='home3'),
    path('about/', views.about, name='about'),
    path('callassistance/', views.assistance, name='callassistance'),


]
