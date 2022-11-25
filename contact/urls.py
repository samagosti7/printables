from django.urls import path
from . import views

urlpatterns = [
    path('', views.contact, name='contact'),
    path('newsletter/', views.newsletter, name='newsletter'),
    # path('newsletter_unsubscribe/', views.newsletter_unsubscribe, name='newsletter_unsubscribe'),
]
