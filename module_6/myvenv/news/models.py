from django.db import models
from django.utils import timezone


class News(models.Model):
    title = models.CharField(max_length=1000, verbose_name='Заголовок')
    description = models.CharField(max_length=1000, verbose_name='Cодержание')
    create_at = models.DateTimeField(editable=False, default=timezone.now())
    updated_at = models.DateTimeField(editable=False, default=timezone.now())
    is_active = models.BooleanField(default=True, verbose_name='Флаг активности')

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        ''' On save, update timestamps '''
        if not self.id:
            self.created = timezone.now()
        self.modified = timezone.now()
        return super(News, self).save(*args, **kwargs)


class Comment(models.Model):
    user_name = models.CharField(max_length=100, verbose_name='Имя пользователя')
    text = models.CharField(max_length=1000, verbose_name='Коментарий')
    create_at = models.DateTimeField(editable=False, default=timezone.now())
    news = models.ForeignKey(News, on_delete=models.CASCADE)

    def __str__(self):
        return self.user_name
