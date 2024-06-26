from django.shortcuts import render ,redirect
from django.http import HttpResponse
from home.models import *


#for give message user alredy existing
from django.contrib import messages

#for only show login page without login not any pages accessible
from django.contrib.auth.decorators import login_required

from django.contrib.auth import authenticate , login , logout

from message.templates import *
from account.templates import *
from explore.templates import *
from reels.templates import *



# Create your views here.
@login_required(login_url='/login')
def home (request):
    user=CustomUser.objects.all()
    is_large_sidebar = True  # Example: this could be based on user preferences or any other logic
    return render(request, 'sidebar.html',context={'user':user , 'is_large_sidebar': is_large_sidebar} )


def logout_page (request):
    logout(request)
    return redirect('/login')


def login_page (request):
     if request.method == 'POST':
        Username= request.POST.get('username')
        Password= request.POST.get('password')

        if not CustomUser.objects.filter(username= Username).exists():
            messages.info(request, "User name is not available")
            return redirect('/login') 
        
        #chek username and password are correct or not using authenticated functions
        check_user=authenticate(username=Username, password=Password)

        #if check_user is not set then pass message to login page
        if check_user is None :
            messages.info(request, "password is not valid")
            return redirect('/login') 
        
        else :
            login(request,check_user)
            print (Username)
            return redirect('home')    


    

     return render(request ,"login/login.html" )


def Register(request):
    if request.method == 'POST':
        #catch all data frome form to an variables
        First_name = request.POST.get('fullname')
        Username= request.POST.get('username')
        Email= request.POST.get('Email')
        Password= request.POST.get('password')
        
        #for find user name alredy existing
        same_uname=CustomUser.objects.filter(username=Username)
        #if exists give a message to ragister form
        if same_uname.exists():
            messages.info(request, "User name already exists")
            return redirect('register') 
        
       


        #give value to objects of User model by using variables
        user= CustomUser.objects.create(
            name=First_name,
           
            username=Username,
            email = Email
        )
        user.set_password(Password)
        user.save()
        print ("account created successfully")
        messages.info(request, "Account Created successfully") 

        return redirect ('home') 
    return render(request,'login/ragister.html')


def Message(request):
    return render(request,'mes.html')

def Notification(request):
    return render(request,'notification.html')

def Search(request):
    return render(request,'search.html')

def Add(request):
    return render(request,'add.html')

# def Account(request):
#     user=CustomUser.objects.all()
#     is_large_sidebar = True 
#     return render(request,'account.html',context={'user':user ,'is_large_sidebar': is_large_sidebar})

# def Reels(request):
#     return render(request,'reels.html')

def Explore(request):
    user=CustomUser.objects.all()
    is_large_sidebar = True 
    return render(request,'explore.html',context={'user':user ,'is_large_sidebar': is_large_sidebar})
