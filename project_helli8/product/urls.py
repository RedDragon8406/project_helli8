from django.urls import path,include
from rest_framework.routers import DefaultRouter
from rest_framework.urlpatterns import format_suffix_patterns

from product import views


# router = DefaultRouter()
# router.register("product", views.UserProductViewSet, basename='products')
urlpatterns = [
    path('product/',views.product_list),
    path('product/<int:pk>',views.product_detail),
    path('product/search',views.search.as_view())
]

urlpatterns = format_suffix_patterns(urlpatterns)