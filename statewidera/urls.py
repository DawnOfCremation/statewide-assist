#from django.conf.urls import url
from django.contrib import admin
from django.urls import path, include
from . import views
from django.conf import settings
from django.conf.urls.static import static
import service.views
import postcode.views
import faq.views



admin.site.site_header = settings.ADMIN_SITE_HEADER



urlpatterns = [
    path('admin/', admin.site.urls),
    path('about/', views.about, name='about'),
    path('contact/', views.contact, name='contact'),
    path('faq/', faq.views.faq, name='faq'),
    #-----------------------------------------------
    path('', service.views.home, name='home'),
    path('post/', service.views.home, name='post'),
    path('services/', service.views.services, name='services'),
    path('', include('contact.urls')),
    path('', include('postcode.urls')),
    path('', include('service.urls')),



] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
