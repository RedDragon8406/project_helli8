from django.db import models
from django.db.models import Q
import os

def get_filename_ext(filepath):
    base_name = os.path.basename(filepath)
    name, ext = os.path.splitext(base_name)
    return name, ext


def upload_image_path(instance, filename):
    name, ext = get_filename_ext(filename)
    final_name = f"{instance.id}-{instance.title}{ext}"
    return f"topics/{final_name}"


class UserTopicManager(models.Manager):
    """Manager for user profiles"""

    def create_topic(self, **kwargs):
        topic = self.model(name=kwargs["title"],img=kwargs["img"])
        topic.save(using=self._db)

        return topic


    def get_topics_product_numbers(self, category_name):
        mmd = self.get_queryset().filter(products__exist__exact=True)
        return mmd.count()
    def get_by_id(self, topic_id):
        qs = self.get_queryset().filter(id=topic_id)
        if qs.count() == 1:
            return qs.first()
        else:
            return None

    def search(self, query):
        lookup = (
                Q(title__icontains=query)
        )
        return self.get_queryset().filter(lookup).distinct()

class UserTopic(models.Model):
    '''database model for users in the system'''
    title=models.CharField(max_length=50)
    img = models.ImageField(upload_to=upload_image_path, null=True, blank=True)
    objects = UserTopicManager()

    def __str__(self):
        """return string representation of our user"""
        return self.title

    class Meta:
        ordering=['title']