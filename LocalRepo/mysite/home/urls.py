from django.contrib import admin
from django.urls import path
from home import views

urlpatterns = [
    path('', views.index, name='home'),
    path('home',views.index, name='home'),
    path('register',views.registerpage, name='register'),
    path('register/userlogin/',views.userlogin, name='login'),
    path('userlogin', views.userlogin, name='login'),
    path('logout/', views.userLogout, name='logout'),
    path('contact', views.contact, name='contact'),
    path('about', views.aboutus, name='about'),
    path('report', views.report, name='report'),
    path('index/', views.index, name='home'),
    path('page/', views.page, name='complaint'),
    path('page', views.page, name='complaint'),
    path('popup/', views.popUp, name='popup'),
    path('records', views.recordPage, name='records'),
    path('report/records/', views.recordPage, name='records'),
    path('home/records/', views.recordPage, name='records'),
    path('records/<pk>/', views.readCrimeReport, name='read_cr'),
    path('create_your_details/', views.createYourDetails, name='create_your_details'),
    path('update_your_details/<int:id>/', views.updateYourDetails, name='update_your_details'),
    path('delete_your_details/<int:id>/', views.deleteYourDetails, name='delete_your_details'),
    path('create_crime_details/', views.createCrimeDetails, name='create_your_details'),
    path('update_crime_details/<pk>/', views.updateCrimeDetails, name='update_your_details'),
    path('delete_your_details/<pk>/', views.deleteCrimeDetails, name='delete_your_details'),
]
