from django.shortcuts import render
from home.models import *
# Create your views here.


def Account(request):
    users = CustomUser.objects.all()  # Fetch all users
    is_large_sidebar = True 
    context = {
        'users': users,
        'is_large_sidebar': is_large_sidebar,
    }
    return render(request,'account.html', context)

