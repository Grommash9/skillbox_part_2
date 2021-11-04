from django.http import HttpResponse
from django.template import loader


def show_todo(request):
    template = loader.get_template('todo.html')
    context = {}
    rendered_page = template.render(context, request)
    return HttpResponse(rendered_page)


def home(request):
    template = loader.get_template('home.html')
    context = {}
    rendered_page = template.render(context, request)
    return HttpResponse(rendered_page)