from django.shortcuts import render
from django.http import HttpResponse

def polls(request, *args, **kwargs):
    return render(request, 'D:/python/skillbox_part_2/module_2/polls/templates/polls.html', {})

def java(request, *args, **kwargs):
    return render(request, 'D:/python/skillbox_part_2/module_2/polls/templates/java.html', {})

def html(request, *args, **kwargs):
    return render(request, 'D:/python/skillbox_part_2/module_2/polls/templates/html.html', {})

def google(request, *args, **kwargs):
    return render(request, 'D:/python/skillbox_part_2/module_2/polls/templates/google.html', {})

def kartoshka(request, *args, **kwargs):
    return render(request, 'D:/python/skillbox_part_2/module_2/polls/templates/kartoshka.html', {})

def valera(request, *args, **kwargs):
    return render(request, 'D:/python/skillbox_part_2/module_2/polls/templates/valera.html', {})
