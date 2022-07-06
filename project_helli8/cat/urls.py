from django.urls import path,include
from rest_framework.routers import DefaultRouter

from cat import views


router = DefaultRouter()
router.register("category", views.UserCatManager)
urlpatterns = [
    path('',include(router.urls))
]