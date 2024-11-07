from django.shortcuts import render, HttpResponse, redirect
from datetime import datetime
from home.models import YourDetail, CrimeDetail
from django.contrib.auth.models import User       
from django.contrib.auth import authenticate,login,logout
from django.http import HttpResponseRedirect
from django.contrib.auth.decorators import permission_required
import random
from mysite.forms import YourDetailsForm, CrimeDetailsForm 

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
        password = request.POST['Password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('complaint')
        else:
            return render(request, 'login.html', {'error': 'Invalid credentials'})
    return render(request, 'login.html')

def report(request):
    if request.method == "POST":
        your_det_form = YourDetailsForm(request.POST)
        cr_det_form = CrimeDetailsForm(request.POST)
        if your_det_form.is_valid() and cr_det_form.is_valid():
            your_det = your_det_form.save()
            cr_det = cr_det_form.save()
            return HttpResponse("Your details and crime report have been registered successfully!!!")
        else:
            return render(request, 'report.html', {'your_det_form': your_det_form, 'cr_det_form': cr_det_form})
    else:
        your_det_form = YourDetailsForm()
        cr_det_form = CrimeDetailsForm()
        return render(request, 'report.html', {'your_det_form': your_det_form, 'cr_det_form': cr_det_form})

def generateRandomId():
    return random.randint(100000,999999)

def popUp(request):
    user = User.objects.all()
    if user is not None:
        return redirect(request,'records')
    return render(request,'popup.html',locals())

def createYourDetails(request):
    if request.method == 'POST':
        form = YourDetailsForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('records')
    else:
        form = YourDetailsForm()
    return render(request, 'records.html', {'form': form})    
        
def recordPage(request):
    print("record is returned here")
    your_det = YourDetail.objects.all()
    print(your_det)
    print(type(your_det))
    cr_det = CrimeDetail.objects.all()
    form = YourDetailsForm()
    return render(request,'records.html',  {'your_det': your_det, 'cr_det': cr_det, 'form': form})

@permission_required('can_create_crime_report')
def createCrimeDetails(request):
    if request.method == 'POST':
        form = CrimeDetailsForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('records')  # redirect to the records list
    else:
        form = CrimeDetailsForm()
    return render(request, 'records.html', {'form': form})

def readCrimeReport(request, pk):
    return render(request, 'records.html', {'pk': pk})

def updateCrimeDetails(request, pk):
    crime_report = CrimeDetail.objects.get(pk=pk)
    if request.method == "POST":
        form = CrimeDetailsForm(request.POST, instance=crime_report)
        if form.is_valid():
            form.save()
            return redirect('records')
    else:
        form = CrimeDetailsForm(instance=crime_report)
    return render(request, 'records.html', {'form': form})

def updateYourDetails(request,id):
    print("this is running 1234567890")
    crime_report = YourDetail.objects.get(pk=id)
    if request.method == "POST":
        form = YourDetailsForm(request.POST, instance=crime_report)
        if form.is_valid():
            form.save()
            return redirect('records')
    else:
        form = YourDetailsForm(instance=crime_report)
    return render(request, 'records.html')

def deleteYourDetails(request, id):
    your_det = YourDetail.objects.get(pk=id)
    your_det.delete()
    return redirect('records')

def deleteCrimeDetails(request, pk):
    cr_det = CrimeDetail.objects.get(pk=pk)
    cr_det.delete()
    return redirect('records')



def userLogout(request):
    logout(request)
    return redirect('index')