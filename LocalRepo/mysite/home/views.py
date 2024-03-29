from django.shortcuts import render, HttpResponse, redirect
from datetime import datetime
from home.models import Report,Userlogin 
from django.contrib.auth.models import User       
from django.contrib.auth import authenticate,login

# Create your views here.
def index(request):
    return render(request,'index.html')

def aboutus(request):
    return render(request,'aboutus.html')

def contact(request):
    return render(request,'contact.html')

def registerpage(request):
    if request.method == 'POST':
        fullname = request.POST.get('full name')
        username = request.POST.get('username')
        pass1 = request.POST.get('password1')
        pass2 = request.POST.get('password2')
        phone = request.POST.get('phone no')
        email = request.POST.get('email')
        if pass1 != pass2:
            return HttpResponse("Your password is incorrect!!"),render(request,'register.html')
        else:
            uname = username
            password = pass1
            myuser = User.objects.create_user(uname,password,email)
            myuser.save()
            print(username,password,email)
            return HttpResponse("User has been created successfully!!!"),redirect(request,'login.html')
    return render(request,'register.html')

def userlogin(request):
    return render(request,'login.html')

def report(request):
    if request.method == "POST":
        reporter_name = request.POST.get('reporter name')
        reporter_email = request.POST.get('reporter email-id')
        criminal_desc = request.POST.get('criminal desc')
        phone = request.POST.get('phone no')
        date_of_report = request.POST.get('date of reporting')
        report = Report(reporter_name=name, reporter_email=email, criminal_desc=desc, phone=phone, date_of_report = datetime.today()) 
        report.save()
        return HttpResponse("Your message has been sent succesfully!!!")       
    return render(request, 'index.html')
