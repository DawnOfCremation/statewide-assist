

from django.urls import path
from . import views


urlpatterns = [
    path('reqassist', views.contact),
    path('snippet', views.snippet_detail),


]
