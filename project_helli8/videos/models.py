import datetime
from time import timezone
from django.core.validators import FileExtensionValidator
from django.db import models
import os
from product.models import UserProduct as Product, UserProduct


def get_filename_ext(filepath):
    base_name = os.path.basename(filepath)
    name, ext = os.path.splitext(base_name)
    return name, ext


def upload_video_path(instance, filename):
    name, ext = get_filename_ext(filename)
    final_name = f"{instance.id}-{instance.title}{ext}"
    return f"videos/{final_name}"

class VideosManager(models.Manager):
    """Manager for user profiles"""

    def create_video(self, title, video):
        video = self.model(title=title,video=video)
        video.save(using=self._db)

        return video


    def CreateVideo(self, title, video):
        """Create and save a superuser with given details"""
        video = self.create_video(title, video)
        video.save(using=self._db)

        return video

class UserVideo(models.Model):
    '''database model for users in the system'''
    title=models.CharField(max_length=100)
    video = models.FileField(upload_to='product/videos/', null=True,
                             validators=[
                                 FileExtensionValidator(allowed_extensions=['MOV', 'avi', 'mp4', 'webm', 'mkv'])])
    date_uploaded = models.DateTimeField(default=datetime.datetime.now())
    product = models.ForeignKey(UserProduct,on_delete=models.CASCADE)

    objects = VideosManager()
    REQUIRED_FIELDS = ['title','video']

    def __str__(self):
        """return string representation of our user"""
        return self.title

