from django.db import models


class UserMainManager(models.Manager):
    """Manager for user profiles"""

    def create_main(self, name, author, desc=None):
        product = self.model(name=name,desc=desc,app=app)
        # profile_img = models.ImageField(upload_to='uploads/', blank=True, null=True)
        main.save(using=self._db)

        return product


class UserMain(models.Model):
    '''database model for users in the system'''
    name=models.CharField(max_length=255)
    author=models.CharField(max_length=255)
    desc=models.TextField()
    image = models.ImageField(upload_to='main/', null=True, blank=True)
    is_there = models.BooleanField(default=False)

    objects = UserMainManager()
    USERNAME_FIELD = 'name'
    REQUIRED_FIELDS = ['name','app']

    def __str__(self):
        """return string representation of our user"""
        return self.name
