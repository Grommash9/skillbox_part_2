from django import forms
from django.utils import timezone
from . import models


class NewsForm(forms.Form):
    title = forms.CharField(max_length=1000)
    description = forms.CharField(max_length=1000)
    is_active = forms.BooleanField()

    def __str__(self):
        return self.title


class NewsForm2(forms.ModelForm):

    class Meta:
        model = models.News
        fields = '__all__'



class Comment(forms.Form):
    user_name = forms.CharField(min_length=5, max_length=30)
    text = forms.CharField(min_length=5, max_length=1000)
