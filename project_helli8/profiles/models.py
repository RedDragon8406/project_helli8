from django.db import models
from django.contrib.auth.models import AbstractBaseUser
from django.contrib.auth.models import PermissionsMixin
from django.contrib.auth.models import BaseUserManager
import os
from product import models as m
def get_filename_ext(filepath):
    base_name = os.path.basename(filepath)
    name, ext = os.path.splitext(base_name)
    return name, ext


def upload_image_path(instance, filename):
    name, ext = get_filename_ext(filename)
    final_name = f"{instance.id}-{instance.title}{ext}"
    return f"products/{final_name}"

def upload_gallery_image_path(instance, filename):
    name, ext = get_filename_ext(filename)
    final_name = f"{instance.id}-{instance.title}{ext}"
    return f"products/galleries/{final_name}"

class UserProfileManager(BaseUserManager):
    """Manager for user profiles"""

    def create_user(self, email, name, img, password=None):
        """Create a new user profile"""
        if not email:
            raise ValueError("User needs an email address")

        email = self.normalize_email(email)
        user = self.model(email=email, name=name, img=img)
        user.set_password(password)
        user.save(using=self._db)

        return user


    def create_superuser(self, email, name, password,img):
        """Create and save a superuser with given details"""
        user = self.create_user(email=email,name=name,img=img)
        user.set_password(password)

        user.is_superuser=True
        user.is_staff=True
        user.save(using=self._db)

        return user



class UserProfile(AbstractBaseUser, PermissionsMixin):
    '''database model for users in the system'''
    email=models.EmailField(max_length=255, unique=True)
    name=models.CharField(max_length=255)
    img = models.ImageField(upload_to='profile/', null=True, blank=True)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    favorite = models.ManyToManyField(m.UserProduct,blank=True)

    objects = UserProfileManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['name']

    def get_full_name(self):
        """retrieve full name of user"""
        return self.name
    def get_short_name(self):
        """retrieve short name of user"""
        return self.name

    def __str__(self):
        """return string representation of our user"""
        return self.email
