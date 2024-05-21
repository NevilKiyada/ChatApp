from django.shortcuts import render
from django.http import HttpResponse

from django.contrib.auth import authenticate , login , logout

# Create your views here.
def home (request):
    return render(request,"sidebar.html",)


def login_page (request):
    return render(request,"login/login.html" )


def Ragister(request):
    return render(request,"login/ragister.html" )