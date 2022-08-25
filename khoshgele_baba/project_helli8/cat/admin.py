from django.contrib import admin

# Register your models here.
from cat import models

admin.site.register(models.UserCat)
