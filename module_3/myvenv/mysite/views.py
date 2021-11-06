import random

from django.http import HttpResponse
from django.shortcuts import render
from django.views.generic import TemplateView


class HomePage(TemplateView):
    template_name = 'home.html'

    def get_context_data(self, **kwargs):
        category_list = ['телефоны', 'мегафоны', 'патисоны', 'мериксоны', 'клариксоны']
        regions_list = ['Киве', 'Полтава', 'Харьков', 'Сидельниково']
        context = super().get_context_data(**kwargs)
        context['category_list'] = category_list
        context['regions_list'] = regions_list

        return context
