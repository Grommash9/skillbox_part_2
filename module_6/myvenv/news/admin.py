from django.contrib import admin
from .import models
# Register your models here.


class NewsAdmin(admin.ModelAdmin):
    list_display = ['id', 'title', 'create_at', 'updated_at', 'is_active']


class NewsComment(admin.ModelAdmin):
    list_display = ['id', 'user_name', 'text', 'create_at', 'news_id']


admin.site.register(models.News, NewsAdmin)
admin.site.register(models.Comment, NewsComment)
