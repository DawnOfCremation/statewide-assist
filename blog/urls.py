from django.contrib import admin
from django.urls import path
from .import views
from .views import allblogs, detail

urlpatterns = [
    path('blog/', views.allblogs, name='allblogs'),
    path('<int:blog_id>/', views.detail, name='detail'),
    #path('nextblog/<int:blog_id>/', views.nextBlog, name='nextblog'),

]
