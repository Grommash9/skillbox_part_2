from django.urls import path, include
from .views import NewsList, AddNews, DetailNews, EditNews, DeleteNews, SuccessfullyEdited

urlpatterns = [
    path('news/', NewsList.as_view()),
    path('news/<int:pk>/', DetailNews.as_view()),
    path('delete/<int:pk>/', DeleteNews.as_view()),
    path('news/new/', AddNews.as_view()),
    path('edit/<int:pk>', EditNews.as_view()),
    path('edited/<int:pk>', SuccessfullyEdited.as_view()),
]
