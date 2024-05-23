from django.db import models
from django.contrib.auth.models import User

from django.db import models
from django.contrib.auth.models import User  # Import the built-in User model

class UserProfile(models.Model):
    user = models.ForeignKey(User , on_delete=models.SET_NULL , null=True , blank= True) 
    name=models.CharField(max_length=100)
    pic=models.ImageField(upload_to=" userimg" , blank=True , null=True )
   
    def __str__(self):
        return f"{self.user.username}'s Profile"


class friemd(models.Model):
    pass