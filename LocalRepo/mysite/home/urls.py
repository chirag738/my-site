from django.contrib import admin
from django.urls import path
from home import views

urlpatterns = [
    path('', views.index, name='home'),
    path('home',views.index, name='home'),
    path('register',views.registerpage, name='register'),
    path('register/userlogin/',views.userlogin, name='login'),
    path('userlogin', views.userlogin, name='login'),
    path('logout/', views.userlogout, name='logout'),
    path('contact/', views.contact, name='contact'),
    path('about/', views.aboutus, name='about'),
    path('report', views.report, name='report'),
    path('index/', views.index, name='home'),
    path('page/', views.page, name='complaint'),
    path('page', views.page, name='complaint'),
    path('popup/', views.popup, name='popup'),
    path('records', views.record, name='records'),
    path('report/records/', views.record, name='records'),
    path('home/records/', views.record, name='records'),
    path('records/create/', views.create_crime_report, name='create_crime_report'),
    path('records/<pk>/', views.read_crime_report, name='read_cr'),
]
