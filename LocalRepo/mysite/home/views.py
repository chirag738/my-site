from django.shortcuts import render, HttpResponse, redirect
from datetime import datetime
from home.models import Report,Userlogin 
from django.contrib.auth.models import User       
from django.contrib.auth import authenticate,login,logout
from django.http import HttpResponseRedirect

# Create your views here.
def index(request):
    return render(request,'index.html')

def aboutus(request):
    return render(request,'aboutus.html')

def contact(request):
    return render(request,'contact.html')

def registerpage(request):
    if request.method == 'POST':
        fullname = request.POST['name']
        username = request.POST['Username']
        email = request.POST['email']
        pass1 = request.POST['password']
        pass2 = request.POST['confirmPassword']
        phone = request.POST['phone']
        if pass1 != pass2:
            return HttpResponse("Your passwords do not match!!")
        if User.objects.filter(username=username).exists():
            return HttpResponse("Username already exists. Please choose a different username.")
        user = User.objects.create_user(username, email, pass1)
        user.save()
        return redirect('userlogin/')
    return render(request,'register.html')

def userlogin(request):
    if request.method == 'POST':
        username = request.POST['Username']
        pass1 = request.POST['Password']
        print(username,pass1)
        user = authenticate(request,username=username,password=pass1)
        if user is not None:
            login(request,user)
            return redirect(request,'/index')
        else:
            return render(request,'login.html')
    return render('/login/')

def report(request):
    if request.method == "POST":
        reporter_name = request.POST.get('name')
        reporter_email = request.POST.get('email')
        criminal_desc = request.POST.get('description')
        phone = request.POST.get('phone')
        date_of_report = request.POST.get('date')
        report = Report(reporter_name=name, reporter_email=email, criminal_desc=desc, phone=phone, date_of_report = datetime.today()) 
        report.save()
        return HttpResponse("Your report has been registered succesfully!!!")       
    return render(request,'report.html')
