from django.shortcuts import render, redirect
from django.conf import settings
import requests
# Create your views here.
from django.core.mail import send_mail, BadHeaderError
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, redirect
from .forms import ContactForm
from django.contrib import messages


def emailView(request):
    if request.method == 'GET':
        form = ContactForm()
    else:
        form = ContactForm(request.POST)
        if form.is_valid():
            ''' Begin reCAPTCHA validation '''
            recaptcha_response = request.POST.get('g-recaptcha-response')
            data = {
                'secret': local_settings.GOOGLE_RECAPTCHA_SECRET_KEY,
                'response': recaptcha_response
            }
            r = requests.post('https://www.google.com/recaptcha/api/siteverify', data=data)
            result = r.json()
            ''' End reCAPTCHA validation '''

            subject = form.cleaned_data['subject']
            your_email = form.cleaned_data['your_email']
            mobile_number = form.cleaned_data['mobile_number']
            message = form.cleaned_data['message']
            package = 'Email: ' + your_email + '   Ph: ' + mobile_number +'   Message: ' + message
            if result['success']:
                print("yes")
                try:
                    send_mail(subject, package, your_email, ['statewidera@gmail.com'],
                    fail_silently=False,)
                except BadHeaderError:
                    return HttpResponse('Invalid header found.')
                return redirect('success')
            else:
                print("No")
            messages.warning(request, 'Invalid reCAPTCHA. Please try again.')


    return render(request, "email.html", {'form': form})

def successView(request):
    #return HttpResponse('Success! Thank you for your message.')
    return render(request, 'contact.html')
