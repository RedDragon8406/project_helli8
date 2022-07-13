from django.contrib import admin

# Register your models here.
from videos import models

admin.site.register(models.UserVideo)
