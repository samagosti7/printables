from django import forms
from .models import Contact, Newsletter


class ContactForm(forms.ModelForm):
    """Contact Form"""

    class Meta:

        model = Contact

        fields = '__all__'

        # labels = {
        #     'name': ('Full Name'),
        #     'email': ('E-mail address'),
        # }


class NewsletterForm(forms.ModelForm):
    """Newsletter Form"""

    class Meta:
        model = Newsletter
        fields = ['email', ]
        # labels = {
        #     'email': 'E-mail Address'
        # }
