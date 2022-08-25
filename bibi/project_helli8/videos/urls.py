from django.urls import path,include
from rest_framework.routers import DefaultRouter

from videos import views
from videos.views import video_list

urlpatterns = [
    path('videos/',video_list)
]