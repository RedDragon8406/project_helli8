from django.db import models


class UserCatManager(models.Manager):
    """Manager for user profiles"""

    def create_cat(self, name):
        cat = self.model(name=name)
        cat.save(using=self._db)

        return cat
    def CreateMain(self, name):
        """Create and save a superuser with given details"""
        cat = self.create_cat(name)

        cat.save(using=self._db)

        return cat



class UserCat(models.Model):
    '''database model for users in the system'''
    name=models.CharField(max_length=255)

    objects = UserCatManager()
    REQUIRED_FIELDS = ['name']

    def __str__(self):
        """return string representation of our user"""
        return self.name
