from django.shortcuts import render, HttpResponse, redirect
from datetime import datetime
from home.models import YourDetail, CrimeDetail 
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
    return render(request,'login.html')
    # return render(request,'register.html')

def details(request):
    if request.method == "POST":
        name1 = request.POST['First Name']
        name2 = request.POST['Middle Name']
        name3 = request.POST['Last Name']
        age = request.POST['age']
        email = request.POST['email id']
        mobile = request.POST['mobile no']
        date = request.POST['date']
        address = request.POST['address']
        your_det = YourDetail(first_name=name1, middle_name=name2, last_name=name3, age=age, email=email, mobile_no=mobile, date=datetime.today()) 
        your_det.save()
        crim_name = request.POST['criminal type']
        nickname = request.POST['criminal nickname']
        cr_type = request.POST['crime type']
        date_crime = request.POST['date of crime']
        cr_age = request.POST['criminal age']
        gender = request.POST['gender']
        cr_mob_no = request.POST['criminal mobile no']
        clue = request.POST['clue about criminal']
        cr_spot = request.POST['crime spot']
        cr_details = CrimeDetail(criminal_name=crim_name, nick_name=nickname, crime_type=cr_type, date_of_crime=date_crime, criminal_age=cr_age, gender=gender, crime_mob_no=cr_mob_no, clue=clue, crime_spot=cr_spot)
        cr_details.save()
        return HttpResponse("The crime details and your details have been saved successfully!!!")
    return render(request,'report.html')
