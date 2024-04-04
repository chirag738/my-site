from django.contrib import admin
from django.urls import path
from home import views

urlpatterns = [
    path('', views.index, name='home'),
    path('home/',views.index, name='home'),
    path('register/',views.registerpage, name='register'),
    path('register/userlogin/',views.userlogin, name='login'),
    path('userlogin/', views.userlogin, name='login'),
    path('contact/', views.contact, name='contact'),
    path('about/', views.aboutus, name='about'),
    path('report/',views.details, name='report'),
    path('index', views.index, name='home'),
    path('page/',views.page, name='complaint'),
]
