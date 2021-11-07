from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
from django.views import generic
from . import models


class AdvertisementListView(generic.ListView):
    model = models.Advertisement
    template_name = 'advertisement_list.html'

    context_object_name = 'advertisement_list'


class AdvertisementDetailView(generic.DetailView):
    model = models.Advertisement

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['catalog_name'] = models.AdvertisementCatalog.get_next_in_order()

        return context
