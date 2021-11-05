from django.urls import path
from .import views

urlpatterns = [
    path('', views.polls, name='polls'),
    path('java/', views.java, name='java'),
    path('html/', views.html, name='html'),
    path('google/', views.google, name='google'),
    path('kartoshka/', views.kartoshka, name='kartoshka'),
    path('valera/', views.valera, name='valera'),
]