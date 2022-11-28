from django.db import models

# Create your models here.


class Contact(models.Model):
    '''Contact model'''
    name = models.CharField(blank=False, null=False, max_length=99)
    email = models.EmailField(blank=False, null=False, max_length=199)
    date = models.DateTimeField(auto_now_add=True)
    topic = models.CharField(max_length=50, null=False, blank=False, default='')
    content = models.TextField(blank=False, null=False, max_length=500)


class Newsletter(models.Model):
    '''Newsletter contact model'''
    first_name = models.CharField(blank=False, null=False, max_length=99)
    email = models.EmailField(blank=False, null=False, max_length=500)
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.email
