from django.shortcuts import render, get_object_or_404
from home.models import *
# Create your views here.


def Account(request):
    luser=request.user
    user = get_object_or_404(CustomUser, username=luser)  
    followers = user.get_followers()
    following = user.get_following()
    fcount =0
    scount = 0
    for follower in followers:
        print (follower)
        fcount += 1
    for followin in following:
        print (followin)
        scount += 1
    context = {
        'users': user,
        'followers': followers,
        'following': following,
        'fcount': fcount,
        'scount': scount,
    }
    return render(request,'account.html', context)

