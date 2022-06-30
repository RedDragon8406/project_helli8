from django.db import models


class UserMainManager(models.Manager):
    """Manager for user profiles"""

    def create_main(self, app):
        main = self.model(app=app)
        main.save(using=self._db)

        return main


class UserMain(models.Model):
    '''database model for users in the system'''
    app=models.CharField(max_length=255)
    # image = models.ImageField(upload_to='main/', null=True, blank=True)

    objects = UserMainManager()
    USERNAME_FIELD = 'app'
    REQUIRED_FIELDS = ['app']

    def __str__(self):
        """return string representation of our user"""
        return self.name
