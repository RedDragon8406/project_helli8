from django.db import models


class UserProductManager(models.Manager):
    """Manager for user profiles"""

    def create_product(self, name, author, desc=None):
        product = self.model(name=name,desc=desc,author=author)
        # profile_img = models.ImageField(upload_to='uploads/', blank=True, null=True)
        product.save(using=self._db)

        return product


    def CreateProduct(self, name, desc, author):
        """Create and save a superuser with given details"""
        product = self.create_product(name,desc,author)

        product.is_there = False
        product.save(using=self._db)

        return product


class UserProduct(models.Model):
    '''database model for users in the system'''
    name=models.CharField(max_length=255)
    author=models.CharField(max_length=255)
    desc=models.TextField()
    image = models.ImageField(upload_to='product/', null=True, blank=True)
    is_there = models.BooleanField(default=False)

    objects = UserProductManager()
    USERNAME_FIELD = 'name'
    REQUIRED_FIELDS = ['name','author']

    def __str__(self):
        """return string representation of our user"""
        return self.name
