from django.urls import path,include
from rest_framework.routers import DefaultRouter

from profiles import views


router = DefaultRouter()
router.register("ViewSet", views.ViewSet, basename='my-viewset')
router.register("profile", views.UserProfileViewSet)
router.register("profile", views.UserProfileViewSet)
urlpatterns = [
    path('sup', views.ApiView.as_view()),
    path('login/',views.UserLoginApiView.as_view()),
    path('',include(router.urls))
]