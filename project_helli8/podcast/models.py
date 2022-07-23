import datetime
from time import timezone
from django.core.validators import FileExtensionValidator
from django.db import models
import os
from product.models import UserProduct as Product, UserProduct


def get_voice_ext(filepath):
    base_name = os.path.basename(filepath)
    name, ext = os.path.splitext(base_name)
    return name, ext


def upload_voice_path(instance, filename):
    name, ext = get_voice_ext(filename)
    final_name = f"{instance.id}-{instance.title}{ext}"
    return f"product/podcast/{final_name}"

class VoiceManager(models.Manager):
    """Manager for user profiles"""

    def create_podcast(self, title, voice):
        video = self.model(title=title,voice=voice)
        video.save(using=self._db)

        return video


    def CreateVideo(self, title, video):
        """Create and save a superuser with given details"""
        video = self.create_video(title, video)
        video.save(using=self._db)

        return video

class UserVoice(models.Model):
    '''database model for users in the system'''
    title=models.CharField(max_length=100)
    voice = models.FileField(upload_to=get_voice_ext, null=True,
                             validators=[
                                 FileExtensionValidator(allowed_extensions=['mp3'])])
    date_uploaded = models.DateTimeField(default=datetime.datetime.now())
    product = models.ForeignKey(UserProduct,on_delete=models.CASCADE,related_name="podcasts")

    objects = VoiceManager()
    REQUIRED_FIELDS = ['title','voice']

    def __str__(self):
        """return string representation of our user"""
        return self.title

