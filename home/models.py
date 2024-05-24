from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin
from django.utils.translation import gettext_lazy as _

class CustomUserManager(BaseUserManager):
    def create_user(self, username, name, email, password=None, **extra_fields):
        if not username:
            raise ValueError('The Username field must be set')
        if not name:
            raise ValueError('The Name field must be set')
        if not email:
            raise ValueError('The Email field must be set')
        
        email = self.normalize_email(email)
        user = self.model(username=username, name=name, email=email, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, username, name, email, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)
        
        if extra_fields.get('is_staff') is not True:
            raise ValueError('Superuser must have is_staff=True.')
        if extra_fields.get('is_superuser') is not True:
            raise ValueError('Superuser must have is_superuser=True.')
        
        return self.create_user(username, name, email, password, **extra_fields)

    def add_friend(self, user, friend):
        user.following.add(friend)
        friend.followers.add(user)

    def remove_friend(self, user, friend):
        user.following.remove(friend)
        friend.followers.remove(user)

class CustomUser(AbstractBaseUser, PermissionsMixin):
    username = models.CharField(max_length=150, unique=True)
    name = models.CharField(max_length=150)
    email = models.EmailField(unique=True)
    mobilenumber = models.CharField(max_length=15, blank=True, null=True)
    bio = models.TextField(blank=True, null=True)
    followers = models.ManyToManyField('self', symmetrical=False, related_name='user_following', blank=True)
    following = models.ManyToManyField('self', symmetrical=False, related_name='user_followers', blank=True)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    date_joined = models.DateTimeField(auto_now_add=True)

    objects = CustomUserManager()

    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = ['name', 'email']

    def __str__(self):
        return self.username

    def add_friend(self, friend):
        self.following.add(friend)
        friend.followers.add(self)

    def remove_friend(self, friend):
        self.following.remove(friend)
        friend.followers.remove(self)

class UserProfile(models.Model):
    user = models.OneToOneField(CustomUser, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    pic = models.ImageField(upload_to="userimg", blank=True, null=True)

    def __str__(self):
        return f"{self.user.username}'s Profile"

class Friendship(models.Model):
    user = models.ForeignKey(CustomUser, related_name='friendships', on_delete=models.CASCADE)
    friend = models.ForeignKey(CustomUser, related_name='friend_of', on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        unique_together = ['user', 'friend']

    def __str__(self):
        return f"{self.user.username} - {self.friend.username}"
