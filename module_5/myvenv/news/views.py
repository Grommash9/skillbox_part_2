from django.shortcuts import render

# Create your views here.
from django.utils import timezone
from django.views import generic, View
from . import models
from . import forms
from django.http import HttpResponseRedirect


class NewsList(generic.ListView):
    model = models.News
    template_name = 'news_list.html'
    context_object_name = 'news_list'
    ordering = ['-create_at']



class AddNews(View):

    def get(self, request):
        news_form = forms.NewsForm()
        return render(request, r'D:\python\skillbox_part_2\module_5\myvenv\news\templates\news\new_news.html', context={'news_form': news_form})

    def post(self, request):
        news_form = forms.NewsForm(request.POST)

        if news_form.is_valid():
            models.News.objects.create(**news_form.cleaned_data)
            return HttpResponseRedirect('/news/')
        return render(request, r'D:\python\skillbox_part_2\module_5\myvenv\news\templates\news\new_news.html', context={'news_form': news_form})


class EditNews(View):
    def get(self, request, pk):
        news_instance = models.News.objects.get(id=pk)
        news_form = forms.NewsForm2(instance=news_instance)
        return render(request, r'D:\python\skillbox_part_2\module_5\myvenv\news\templates\news\edit_news.html', context={'news_form': news_form, 'pk': pk, 'news_instance' : news_instance})

    def post(self, request, pk):
        news_instance = models.News.objects.get(id=pk)
        news_form = forms.NewsForm2(request.POST, instance=news_instance)
        if news_form.is_valid():
            news_instance.updated_at = timezone.now()
            news_form.save()
        return render(request, r'D:\python\skillbox_part_2\module_5\myvenv\news\templates\news\successfully_edited.html',
                      context={'news_form': news_form, 'pk': pk, 'news_instance': news_instance})


class SuccessfullyEdited(generic.DetailView):
    model = models.News
    template_name = r'D:\python\skillbox_part_2\module_5\myvenv\news\templates\news\successfully_edited.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['comments_form'] = forms.Comment()
        context['comments_list'] = models.Comment.objects.all().filter(news_id=self.object.id).order_by('-create_at')
        return context

    def post(self, request, pk):
        comments_form = forms.Comment(request.POST)

        if comments_form.is_valid():
            models.Comment.objects.create(**comments_form.cleaned_data, news_id=pk)
            return HttpResponseRedirect(f'/news/{pk}')
        return render(request, r'D:\python\skillbox_part_2\module_5\myvenv\news\templates\news\successfully_edited.html',
                      context={'comments_form': comments_form})

class DeleteNews(View):

    def get(self, request, pk):
        models.News.objects.filter(id=pk).delete()
        return render(request, r'D:\python\skillbox_part_2\module_5\myvenv\news\templates\news\deleted.html')



class DetailNews(generic.DetailView):

    model = models.News
    template_name = r'D:\python\skillbox_part_2\module_5\myvenv\news\templates\news\detail_news.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['comments_form'] = forms.Comment()
        context['comments_list'] = models.Comment.objects.all().filter(news_id=self.object.id).order_by('-create_at')
        return context

    def post(self, request, pk):
        comments_form = forms.Comment(request.POST)

        if comments_form.is_valid():
            models.Comment.objects.create(**comments_form.cleaned_data,news_id=pk)
            return HttpResponseRedirect(f'/news/{pk}')
        return render(request, r'D:\python\skillbox_part_2\module_5\myvenv\news\templates\news\detail_news.html',
                      context={'comments_form': comments_form})



