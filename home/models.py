from django.db import models
from django.contrib.auth.models import User

from django.db import models
from django.contrib.auth.models import User  # Import the built-in User model

class UserProfile(models.Model):
    user = models.ForeignKey(User , on_delete=models.SET_NULL , null=True , blank= True) 
   
    # bio = models.TextField(blank=True)  # Allow for empty bios
    # gender = models.CharField(max_length=10, choices=[('M', 'Male'), ('F', 'Female'), ('O', 'Other')], blank=True)  # Gender choices
    # profile_picture = models.ImageField(upload_to='profile_pics/', blank=True)  # Use ImageField for profile pictures

    def __str__(self):
        return f"{self.user.username}'s Profile"
