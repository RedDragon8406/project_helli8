from django.db import models
import os
from cat.models import UserCat
from topic.models import UserTopic


def get_filename_ext(filepath):
    base_name = os.path.basename(filepath)
    name, ext = os.path.splitext(base_name)
    return name, ext


def upload_image_path(instance, filename):
    name, ext = get_filename_ext(filename)
    final_name = f"{instance.id}-{instance.name}{ext}"
    return f"products/{final_name}"


class UserProductManager(models.Manager):
    """Manager for user profiles"""

    def create_product(self, **kwargs):
        product = self.model(name=kwargs["name"], desc=kwargs["desc"], author=kwargs["author"], img=kwargs["img"],
                             exist=kwargs["exist"])
        # product.categories.set(kwargs["cat"])
        product.save(using=self._db)

        return product

    def CreateProduct(self, name, desc, author, img):
        """Create and save a superuser with given details"""
        product = self.create_product(name, desc, author, img)
        product.is_there = False
        product.save(using=self._db)

        return product

    def get_active_products(self):
        return self.get_queryset().filter(is_there=True)

    def get_products_by_category(self, category_name):
        return self.get_queryset().filter(categories__name__iexact=category_name, is_there=True)

    def get_by_id(self, product_id):
        qs = self.get_queryset().filter(id=product_id)
        if qs.count() == 1:
            return qs.first()
        else:
            return None

    def search(self, query):
        lookup = (
                models.Q(name__icontains=query) |
                models.Q(desc__icontains=query) |
                models.Q(tag__title__icontains=query)
        )
        return self.get_queryset().filter(lookup, is_there=True).distinct()


from profiles import models as m

class UserProduct(models.Model):
    '''database model for users in the system'''
    name = models.CharField(max_length=255)
    author = models.CharField(max_length=255)
    mani = models.ForeignKey(m.UserProfile, on_delete=models.CASCADE, blank=True, null=True)
    desc = models.TextField()
    img = models.ImageField(upload_to=upload_image_path, null=True, blank=True)
    categories = models.ManyToManyField(UserCat, blank=True)
    date = models.DateTimeField(auto_now_add=True)
    topic = models.ForeignKey(UserTopic, on_delete=models.CASCADE, related_name="products")
    # rate = models.SmallIntegerField(blank=True)

    exist = models.BooleanField(default=False)

    objects = UserProductManager()

    def __str__(self):
        """return string representation of our user"""
        return self.name

    class Meta:
        ordering = ['name']
