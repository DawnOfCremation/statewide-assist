from django.shortcuts import render
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
            subject = form.cleaned_data['subject']
            your_email = form.cleaned_data['your_email']
            mobile_number = form.cleaned_data['mobile_number']
            message = form.cleaned_data['message']
            package = 'Email: ' + your_email + 'Ph: ' + mobile_number +'Message: ' + message
            try:
                send_mail(subject, package, your_email, ['damians@gmail.com'],
                fail_silently=False,)
            except BadHeaderError:
                return HttpResponse('Invalid header found.')
            return redirect('success')
    return render(request, "email.html", {'form': form})

def successView(request):
    #return HttpResponse('Success! Thank you for your message.')
    return render(request, 'contact.html')
