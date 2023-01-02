from django.urls import path
from . import views

urlpatterns = [
    path('', views.blog, name='blog'),
    path('add_post', views.add_post, name='add_post'),
    path('delete_post/<slug:post>/', views.delete_post, name='delete_post'),
    path('edit_post/<slug:post>/', views.edit_post, name='edit_post'),
    path('<slug:post>/', views.post_detail, name='post_detail'),

]