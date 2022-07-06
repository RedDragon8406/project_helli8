from django.db import models
import os

from cat.models import UserCat
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


class UserProductManager(models.Manager):
    """Manager for user profiles"""

    def create_product(self, name, author, img, desc=None):
        product = self.model(name=name,desc=desc,author=author,img=img)
        product.save(using=self._db)

        return product


    def CreateProduct(self, name, desc, author, img):
        """Create and save a superuser with given details"""
        product = self.create_product(name, desc, author, img)
        product.is_there = False
        product.save(using=self._db)

        return product


class UserProduct(models.Model):
    '''database model for users in the system'''
    name=models.CharField(max_length=255)
    author=models.CharField(max_length=255)
    desc=models.TextField()
    img = models.ImageField(upload_to='product/', null=True, blank=True)
    categories = models.ManyToManyField(UserCat, blank=True)


    is_there = models.BooleanField(default=False)

    objects = UserProductManager()
    USERNAME_FIELD = 'name'
    REQUIRED_FIELDS = ['name','author']

    def __str__(self):
        """return string representation of our user"""
        return self.name

