from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path
from home.views import *
from message.views import *
<<<<<<< HEAD
=======
from account.views import *
from reels.views import *
from django.conf.urls.static import static
>>>>>>> 1b4f615d5a16743a371c3c5925f39469d694cd47
from django.contrib.staticfiles.urls import staticfiles_urlpatterns


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home, name='home'),
    path('home', home, name='home'),
    path('search', Search, name='search'),
    path('add', Add, name='add'),
    path('account', Account, name='account'),
    path('reels', Reels, name='reels'),
    path('explore', Explore, name='explore'),
    path('messages', Message, name='messages'),
    path('notification', Notification, name='notification'),
    path('login', login_page, name='login_page'),
    path('logout', logout_page, name='logout'),
    path('register', Register, name='Register'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
urlpatterns += staticfiles_urlpatterns()
