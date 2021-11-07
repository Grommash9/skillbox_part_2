from django.urls import path, include
from .views import AdvertisementListView, AdvertisementDetailView

urlpatterns = [
    path('olx/', AdvertisementListView.as_view(), name='advertisement'),
    path('olx/<int:pk>', AdvertisementDetailView.as_view(), name='advertisement-detail')

]
