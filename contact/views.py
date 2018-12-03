import json
import urllib
from django.shortcuts import render, redirect
from django.conf import settings

# Create your views here.
from django.core.mail import send_mail, BadHeaderError
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, redirect
from .forms import ContactForm


def emailView(request):
    if request.method == 'GET':
        form = ContactForm()
    else:
        form = ContactForm(request.POST)
        if form.is_valid():
            ''' Begin reCAPTCHA validation '''
            recaptcha_response = request.POST.get('g-recaptcha-response')
            url = 'https://www.google.com/recaptcha/api/siteverify'
            values = {
                'secret': local_settings.GOOGLE_RECAPTCHA_SECRET_KEY,
                'response': recaptcha_response
            }
            data = urllib.parse.urlencode(values).encode()
            req =  urllib.request.Request(url, data=data)
            response = urllib.request.urlopen(req)
            result = json.loads(response.read().decode())
            ''' End reCAPTCHA validation '''

            subject = form.cleaned_data['subject']
            your_email = form.cleaned_data['your_email']
            mobile_number = form.cleaned_data['mobile_number']
            message = form.cleaned_data['message']
            package = 'Email: ' + your_email + 'Ph: ' + mobile_number +'Message: ' + message
            try:
                send_mail(subject, package, your_email, ['damians@gmail.com'],
                fail_silently=False,)
            except BadHeaderError:
                messages.error(request, 'Invalid reCAPTCHA. Please try again.')
                return HttpResponse('Invalid header found.')
            return redirect('success')
    return render(request, "email.html", {'form': form})

def successView(request):
    #return HttpResponse('Success! Thank you for your message.')
    return render(request, 'contact.html')
