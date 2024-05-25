from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path
from home.views import *
from message.views import *
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
