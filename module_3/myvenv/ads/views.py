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
        return HttpResponse('запрос на создание новой записи успешно выполнен')


class About(TemplateView):
    template_name = 'about.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['company_name'] = 'Фуркочка'
        context['about'] = 'Нашей комании уже 12 лет и все это время мы плохо делаем задания по питону, а все из-за' \
                           'нечеткого ТЗ, пожалуйста когда отправляете ТЗ прочитайте его хотя бы, с уважением ваши' \
                           ' Фуркочка'
        return context

class Contacts(TemplateView):
    template_name = 'contacts.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['phone'] = '+312318212523'
        context['adress'] = 'ул. Домодедова строение 25, корпус 1'
        context['telegram'] = '@furcko4ka'
        context['viber'] = '+712318212523'
        return context