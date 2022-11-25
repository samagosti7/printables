from django import forms
from .models import Contact, Issue, Newsletter
from django.utils.translation import gettext_lazy as _


class ContactForm(forms.ModelForm):
    """Contact Form"""

    class Meta:

        model = Contact

        fields = (
            'full_name', 'email', 'content',
        )

        labels = {
            'full_name': _('Full Name'),
            'email': _('E-mail address'),
            'content': _('Select Issue:'),
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        issue = Issue.objects.all()
        issue_text = [(i.id, i.get_text()) for i in issue]

        self.fields['issue'].choices = issue_text


class NewsletterForm(forms.ModelForm):
    """Newsletter Form"""

    class Meta:
        model = Newsletter
        fields = ['email', ]
        labels = {
            'email': 'E-mail Address'
        }
