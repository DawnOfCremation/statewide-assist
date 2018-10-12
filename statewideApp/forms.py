
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Submit
from django import forms
from.models import Snippet
from django.core.validators import RegexValidator

class NameWidget(forms.MultiWidget):

    def __init__(self, attrs=None):
        super().__init__([
            forms.TextInput(),
            forms.TextInput()
        ], attrs)

    def decompress(self, value):
        # 'firstvalue secondvalue'
        if value:
            return value.split(' ')
        return ['first name','surname']
            # ['firstcalue','secondvalue']

class NameField(forms.MultiValueField):

    widget = NameWidget

    def __init__(self, *args, **kwargs):

        fields = (
            forms.CharField(validators=[
                RegexValidator(r'[a-zA-Z]+', message='Enter a valid first name (only letters)')
            ]), # popycock
            forms.CharField(validators=[
                RegexValidator(r'[a-zA-Z]+', message='Enter a valid second name (only letters)')
            ]) # twaddle
        )
        super().__init__(fields, *args, **kwargs)

    def compress(self, data_list):
        # data_list = ['popycock','twaddle']
        # data_list = ['first value','second value']
        return f'{data_list[0]} {data_list[1]}'



class  ContactForm(forms.Form):
    name = NameField()
    #name = forms.CharField()
    email = forms.EmailField(label ="E-Mail")
    category = forms.ChoiceField(choices = [('question', 'Question'), ('other', 'Other')])
    subject = forms.CharField(required=False)
    body = forms.CharField(widget=forms.Textarea)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.helper = FormHelper
        self.helper.form_method = 'post'

        self.helper.layout = Layout(
            'name',
            'email',
            'category',
            'subject',
            'body',
            Submit('submit','Submit', css_class='btn-success' )
        )

class SnippetForm(forms.ModelForm):

    class Meta:
        model = Snippet
        fields = ('name', 'body')
