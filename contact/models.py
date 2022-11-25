from django.db import models

# Create your models here.


class Contact(models.Model):
    '''Contact model'''
    full_name = models.CharField(blank=False, null=False, max_length=99)
    email = models.EmailField(blank=False, null=False, max_length=199)
    date = models.DateTimeField(auto_now_add=True)

    content = models.TextField(blank=False, null=False, max_length=500)
    issue = models.ForeignKey("Issue", blank=True, null=True, on_delete=models.SET_NULL)

    def __str__(self):
        return self.name + ", " + self.email


class Issue(models.Model):
    '''Issue model for contact form'''

    issue = models.CharField(blank=True, null=True, max_length=99)
    description = models.TextField(blank=True, null=True, max_length=500)

    def __str__(self):
        return self.issue

    def __get_description__(self):
        return self.description


class Newsletter(models.Model):
    '''Newsletter contact model'''
    first_name = models.CharField(blank=False, null=False, max_length=99)
    email = models.EmailField(blank=False, null=False, max_length=500)
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.email
