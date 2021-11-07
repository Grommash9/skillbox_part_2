from django.contrib import admin
from . import models


# Register your models here.


@admin.register(models.Advertisement)
class AdvertisementAdmin(admin.ModelAdmin):
    pass


@admin.register(models.AdvertisementSeller)
class AdvertisementAdmin(admin.ModelAdmin):
    pass


@admin.register(models.AdvertisementCatalog)
class AdvertisementAdmin(admin.ModelAdmin):
    pass