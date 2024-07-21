from django.shortcuts import render, HttpResponse, redirect
from datetime import datetime
from home.models import YourDetail, CrimeDetail 
from django.contrib.auth.models import User       
from django.contrib.auth import authenticate,login,logout
from django.http import HttpResponseRedirect
import random

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
    return render(request,'register.html',locals())

def page(request):
    return render(request,'page.html')

def userlogin(request):
    if request.method == 'POST':
        username = request.POST['Username']
        pass1 = request.POST['Password']
        print(username,pass1)
        user = authenticate(request,username=username,password=pass1)
        if user is not None:
            login(request,user)
        # url = "/"
        # return HttpResponseRedirect(url)
            return redirect('/page')
        else:
            return render(request,'login.html')
    return render(request,'login.html',locals())
    # return render(request,'register.html')

def report(request):
    if request.method == "POST":
        name1 = request.POST.get('First Name')
        name2 = request.POST.get('Middle Name')
        name3 = request.POST.get('Last Name')
        age = request.POST.get('age')
        email = request.POST.get('email id')
        mobile = request.POST.get('mobile no')
        date = request.POST.get('date')
        address = request.POST.get('address') 
        if your_det.is_valid():
            your_det = YourDetail.objects.create_user(
                name1=first_name,
                name2=middle_name,
                name3=last_name,
                age=age,
                email=email_id,
                date=date,
                mobile=mobile_no,
                address=address
            )
            your_det.save()
            return HttpResponse(request,"Your details has been registered successfully!!!")
        case_id = generate_random_id()
        crim_name = request.POST.get('criminal type')
        nickname = request.POST.get('criminal nickname')
        cr_type = request.POST.get('crime type')
        date_crime = request.POST.get('date of crime')
        cr_age = request.POST.get('criminal age')
        gender = request.POST.get('gender')
        cr_mob_no = request.POST.get('criminal mobile no')
        clue = request.POST.get('clue about criminal')
        cr_spot = request.POST.get('crime spot')
        case_status = "Pending"
        if cr_details.is_valid():
            cr_details = CrimeDetail.objects.create_user(
                case_id=case_id,
                crim_name=criminal_name,
                nickname=nick_name,
                cr_type=crime_type,
                date_crime=date_of_crime,
                cr_age=criminal_age,
                gender=gender,
                cr_mob_no=crime_mob_no,
                clue=clue,
                cr_spot=crime_spot,
                case_status=cs_status
            )
            cr_details.save()
            return redirect('popup.html')
    return render(request,'report.html',locals())

def generate_random_id():
    return random.randint(100000,999999)

def popup(request):
    if user is not None:
        return redirect(request,'records')
    return render(request,'popup.html',locals())

def record(request):
    return render(request,'records.html')