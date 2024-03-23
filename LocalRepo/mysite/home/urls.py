from django.contrib import admin
from django.urls import path
from home import views

urlpatterns = [
    path('', views.registerpage, name='register'),
    path('userlogin', views.userlogin, name='login'),
    path('index', views.index, name='index'),
    path('contact', views.contact, name='contact'),
    path('about', views.aboutus, name='about'),
]
