from django.contrib import admin
from django.urls import path, include
from . import views


urlpatterns = [
    path('', views.HomeAds.as_view()),
    path('about/', views.About.as_view()),
    path('contacts/', views.Contacts.as_view())
]

