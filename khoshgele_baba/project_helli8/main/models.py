from django.db import models


class UserMainManager(models.Manager):
    """Manager for user profiles"""

    def create_main(self, app):
        main = self.model(app=app)
        main.save(using=self._db)

        return main
    def CreateMain(self, app):
        """Create and save a superuser with given details"""
        main = self.create_product(app)

        main.save(using=self._db)

        return main



class UserMain(models.Model):
    '''database model for users in the system'''
    app=models.CharField(max_length=255)

    objects = UserMainManager()
    REQUIRED_FIELDS = ['app']

    def __str__(self):
        """return string representation of our user"""
        return self.app
