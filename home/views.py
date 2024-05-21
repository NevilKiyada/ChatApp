from django.shortcuts import render
from django.http import HttpResponse

from django.contrib.auth import authenticate , login , logout



# Create your views here.
def home (request):
    is_large_sidebar = True  # Example: this could be based on user preferences or any other logic
    return render(request, 'sidebar.html', {'is_large_sidebar': is_large_sidebar})


def login_page (request):
    return render(request,"login/login.html" )


def Ragister(request):
    return render(request,"login/ragister.html" )