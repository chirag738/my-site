from django.shortcuts import render, HttpResponse
from datetime import datetime
from home.models import Report,Userlogin 
from django.contrib.auth.models import User       

# Create your views here.
def index(request):
    return render(request,'index.html')

def aboutus(request):
    return render(request,'aboutus.html')

def contact(request):
    return render(request,'contact.html')

def registerpage(request):
    return render(request,'register.html')

def userlogin(request):
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')
        print(username,password)
        user = authenticate(username=username, password=password)
        if user is not None:
            return redirect("index.html")
        else:
            return render(request,'login.html')
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
        messages.success(request,'Your message has been sent')       
    return render(request, 'index.html')
