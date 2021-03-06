from django import forms


class ContactForm(forms.Form):
    your_email = forms.EmailField(label='Your email', max_length=100, required=True)
    mobile_number = forms.CharField(label='Your Mobile Number', max_length=9, required=True)
    subject = forms.CharField(label='Subject', max_length=100, required=True)
    message = forms.CharField(label='Your message', max_length=400, widget=forms.Textarea, required=True)
