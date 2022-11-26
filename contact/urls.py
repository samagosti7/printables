from django.urls import path
from . import views

urlpatterns = [
    path('contact_us', views.contact_us, name='contact_us'),
    path('newsletter', views.newsletter, name='newsletter'),
    # path('newsletter_unsubscribe/', views.newsletter_unsubscribe, name='newsletter_unsubscribe'), 
]