from django.db import models

# Create your models here.


class Advertisement(models.Model):
    title = models.CharField(max_length=1000, verbose_name='Заголовок')
    discription = models.CharField(max_length=1000, verbose_name='Описание')
    price = models.IntegerField(verbose_name='Цена')
    end_data = models.DateTimeField()
    create_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    views_count = models.IntegerField(verbose_name='количество просмотров', default=0, editable=False)
    seller_data = models.ForeignKey('AdvertisementSeller', default=None, null=None, on_delete=models.CASCADE, related_name='advertisement')
    catalog_data = models.ForeignKey('AdvertisementCatalog', default=None, null=None, on_delete=models.CASCADE,
                                    related_name='advertisement')

    def __str__(self):
        return self.title



class AdvertisementSeller(models.Model):
    name = models.CharField(max_length=1000, verbose_name='Имя')
    contact_phone = models.CharField(max_length=20, verbose_name='Номер телефона')
    email = models.CharField(max_length=40, verbose_name='Имейл')

    def __str__(self):
        return self.name


class AdvertisementCatalog(models.Model):
    catalog_name = models.CharField(max_length=1000, verbose_name='Название катеории')

    def __str__(self):
        return self.catalog_name



