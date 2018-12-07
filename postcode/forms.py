from django import forms


class PostcodeForm(forms.Form):
   postcode = forms.CharField(max_length=4)
