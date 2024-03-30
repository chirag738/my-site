from django.shortcuts import render, HttpResponse, redirect
from datetime import datetime
from home.models import Report,Userlogin 
from django.contrib.auth.models import User       
from django.contrib.auth import authenticate,login,logout

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
        email = request.POST.get('email')
        pass1 = request.POST.get('password1')
        pass2 = request.POST.get('password2')
        phone = request.POST.get('email')
        if pass1 != pass2:
            return HttpResponse("Your password does not match!!"),render(request,'register.html')
        else:
            user = User.objects.create_user(username,pass1,email)
            user.save()
            return HttpResponse("User has been created successfully!!!"), redirect(request,'login.html')
    return render(request,'register.html')

def userlogin(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        pass1 = request.POST.get('password')
        print(username,pass1)
        user = authenticate(request,username=username,password=pass1)
        if user is not None:
            login(request,user)
            return HttpResponse("User has logged in successfully!!!"),redirect('index.html')
        else:
            return HttpResponse("Username or password is invalid."),render(request,'login.html')
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
        return HttpResponse("Your report has been registered succesfully!!!")       
    return render(request,'report.html')
