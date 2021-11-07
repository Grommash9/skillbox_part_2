from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
from django.views import generic
from . import models


class AdvertisementListView(generic.ListView):
    model = models.Advertisement
    template_name = 'advertisement_list.html'

    def get_context_data(self, **kwargs):

        context = super().get_context_data(**kwargs)
        catalogs_dict = dict()
        for catalogs in list(models.AdvertisementCatalog.objects.values()):
            catalogs_dict[catalogs['id']] = catalogs['catalog_name']
        context['catalogs_dict'] = catalogs_dict
        return context


class AdvertisementDetailView(generic.DetailView):
    model = models.Advertisement

    def get_context_data(self, **kwargs):


        context = super().get_context_data(**kwargs)
        catalogs_dict = dict()
        for catalogs in list(models.AdvertisementCatalog.objects.values()):
            catalogs_dict[catalogs['id']] = catalogs['catalog_name']
        context['catalogs_dict'] = catalogs_dict
        users_dict = dict()
        for users in list(models.AdvertisementSeller.objects.values()):
            users_dict[catalogs['id']] = {'name': users['name'],
                                             'contact_phone': users['contact_phone'],
                                             'email': users['email']}
        context['users_dict'] = users_dict
        return context

    def get_object(self, queryset=None):
        obj = super().get_object()
        obj.views_count += 1
        obj.save()
        return obj
