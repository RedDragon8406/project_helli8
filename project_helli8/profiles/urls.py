from django.urls import path

from profiles import views

urlpatterns = [
    path('sup', views.ApiView.as_view()),
]