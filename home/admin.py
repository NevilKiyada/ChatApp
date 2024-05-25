from django.contrib import admin
from .models import *
# Register your models here.


from .models import CustomUser  # Correctly import the models

admin.site.register(CustomUser)
