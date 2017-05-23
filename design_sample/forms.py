from django import forms

class ContactForm(forms.Form):
    first_name = forms.CharField(error_messages={'required': 'First name required'})
    last_name = forms.CharField(error_messages={'required': 'Last name required'})
    email = forms.EmailField(error_messages={'required': 'Email required', 'invalid': 'Must be email'})
    phone_no = forms.RegexField(required=False, regex=r'(\(\+84\)\ ?|0)\d{9,10}',
            error_messages={'invalid': 'Phone number must be in the correct format'})
    title = forms.CharField(error_messages={'required': 'Title required'})
    content = forms.CharField(error_messages={'required': 'Content required'})
