from django.contrib import admin
from product.models import UserProduct
class ProductAdmin(admin.ModelAdmin):
    list_display = ['__str__','exist', 'author','date']
    list_editable = ['exist','author']
    list_filter = ['exist','author']
    search_fields = ['title','description','author']
    ordering = ['date']
    list_per_page = 10
    class Meta:
        model = UserProduct


admin.site.register(UserProduct, ProductAdmin)
