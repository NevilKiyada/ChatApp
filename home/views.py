from django.shortcuts import render ,redirect
from django.http import HttpResponse
from home.models import *


#for give message user alredy existing
from django.contrib import messages

from django.contrib.auth import authenticate , login , logout

# Create your views here.
def home (request):
    return render(request,"sidebar.html",)


def login_page (request):
    return render(request,"login/login.html" )


def Register(request):
    if request.method == 'POST':
        #catch all data frome form to an variables
        First_name = request.POST.get('fullname')
        
        Username= request.POST.get('username')
        Email= request.POST.get('Email')
        Password= request.POST.get('password')
        # mobileno= request.POST.get('Mobile-no')
        # bioo= request.POST.get('bio')
        # gender= request.POST.get('gender')
       

        #for find user name alredy existing
        same_uname=User.objects.filter(username=Username)
        #if exists give a message to ragister form
        if same_uname.exists():
            messages.info(request, "User name already exists")
            return redirect('/Register/') 

        #give value to objects of User model by using variables
        user= User.objects.create(
            first_name=First_name,
            username=Username,
            email = Email
        )
        user.set_password(Password)
        user.save()
        print(Username)
        messages.info(request, "Account Created successfully") 

        return redirect ('')
    return render(request,'login/ragister.html')