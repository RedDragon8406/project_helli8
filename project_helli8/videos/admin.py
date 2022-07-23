from django.contrib import admin

# Register your models here.
from videos import models


class ProductAdmin(admin.ModelAdmin):
    list_display = ['title','video']
    list_editable = ['video']
    list_filter = ['title']
    search_fields = ['name','__str__']
    list_per_page = 10
    class Meta:
        model = models.UserVideo
admin.site.register(models.UserVideo,ProductAdmin)
