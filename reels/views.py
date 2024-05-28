from django.shortcuts import render , get_object_or_404

from home.models import CustomUser , Follow 

# Create your views here.


def Reels (request):
    luser=request.user
    user = get_object_or_404(CustomUser, username=luser)  
    followers = user.get_followers()
    following = user.get_following()
    for follower in followers:
        print (followers)

    context = {
        'users': user,
        'followers': followers,
        'following': following,
    }
    return render(request, 'reels.html', context)
