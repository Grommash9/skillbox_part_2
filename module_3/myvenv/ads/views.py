import random

from django.http import HttpResponse
from django.shortcuts import render
from django.views.generic import TemplateView

calls_counter = [0]


class HomeAds(TemplateView):
    template_name = 'ads_home.html'

    def get_context_data(self, **kwargs):
        ads_list = ['элемент списка', 'картошка', 'морква', 'порква', 'горква']
        random_list = []
        for x in range(0, 5):
            random_list.append(random.choice(ads_list))
        context = super().get_context_data(**kwargs)
        context['ads_list'] = random_list
        context['calls'] = calls_counter[0]
        calls_counter[0] += 1
        return context

    def post(self, request, *args, **kwargs):
        print('yes done')
        return 0
