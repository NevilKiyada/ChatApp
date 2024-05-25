from django.shortcuts import render
from home.models import *
# Create your views here.


def re (request,username):
   
    users = CustomUser.objects.all()  # Fetch all users
    context = {
        'users': users,
    }
    return render(request, 'reels.html', context)
