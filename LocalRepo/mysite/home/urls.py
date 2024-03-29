from django.contrib import admin
from django.urls import path
from home import views

urlpatterns = [
    path('', views.index, name='index'),
    path('register',views.registerpage, name='register'),
    path('userlogin', views.userlogin, name='login'),
    path('contact', views.contact, name='contact'),
    path('about', views.aboutus, name='about'),
]
