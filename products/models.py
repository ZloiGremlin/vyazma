# vim:fileencoding=utf-8
from django.db import models
from django.db.models import permalink
from mptt.fields import TreeForeignKey
from mptt.models import MPTTModel
from products.utils import get_file_path
from shop.models_bases import BaseProduct
from sorl.thumbnail import ImageField


class Category(MPTTModel):
    class MPTTMeta:
        order_insertion_by = ['sort']

    class Meta(object):
        verbose_name = u'Категория'
        verbose_name_plural = u'Категории'

    parent = TreeForeignKey('self', null=True, blank=True, related_name='children', verbose_name=u'Родительская категория')
    name = models.CharField(max_length=255, blank=False, null=False, verbose_name=u'Название')
    url = models.CharField(max_length=255, verbose_name=u'Адрес(URL)', unique=True)
    description = models.TextField(blank=True, verbose_name=u'Описание категории')
    sort = models.IntegerField(verbose_name=u'Приоритет', default=10, help_text=u'Чем меньше значение тем товар выше в списке')
    image = ImageField(upload_to=get_file_path, verbose_name=u'Изображение', blank=True, null=True)

    def __unicode__(self):
        return self.name

    @permalink
    def get_absolute_url(self):
        return 'category', (self.url,), {}


class Region(models.Model):

    class Meta(object):
        verbose_name = u'Регион'
        verbose_name_plural = u'Регионы'
        ordering = ['sort', 'name']

    name = models.CharField(max_length=255, blank=False, null=False, verbose_name=u'Название')
    url = models.CharField(max_length=255, verbose_name=u'Адрес(URL)', unique=True)
    description = models.TextField(blank=True, verbose_name=u'Описание категории')
    sort = models.IntegerField(verbose_name=u'Приоритет', default=10, help_text=u'Чем меньше значение тем товар выше в списке')

    def __unicode__(self):
        return self.name

    @permalink
    def get_absolute_url(self):
        return 'region', (self.url,), {}


class Trader(models.Model):

    class Meta(object):
        verbose_name = u'Продавец'
        verbose_name_plural = u'Продавцы'
        ordering = ['sort', 'name']

    name = models.CharField(max_length=255, blank=False, null=False, verbose_name=u'Название')
    url = models.CharField(max_length=255, verbose_name=u'Адрес(URL)', unique=True)
    region = models.ForeignKey(Region, verbose_name=u'Местоположение', related_name='traders')
    description = models.TextField(blank=True, verbose_name=u'Описание категории')
    sort = models.IntegerField(verbose_name=u'Приоритет', default=10, help_text=u'Чем меньше значение тем товар выше в списке')
    image = ImageField(upload_to=get_file_path, verbose_name=u'Изображение', blank=True, null=True)

    def __unicode__(self):
        return self.name

    @permalink
    def get_absolute_url(self):
        return 'trader', (self.url,), {}


class Product(BaseProduct):
    class Meta:
        ordering = ['sort', 'unit_price']
        verbose_name = u'Товар'
        verbose_name_plural = u'Товары'

    category = TreeForeignKey('Category', verbose_name=u'Категория', related_name='products', null=True, blank=True)
    trader = models.ForeignKey('Trader', verbose_name=u'Продавец', related_name='products')
    description = models.TextField(verbose_name=u'Описание товара', null=True, blank=True)
    sort = models.IntegerField(default=100, verbose_name=u'Приоритет')

    def __unicode__(self):
        return self.name

    def get_price(self):
        return self.unit_price

    def get_main_image(self):
        images = self.images.all()
        if images:
            return images[0]
        return None


    @permalink
    def get_absolute_url(self):
            return 'product_details', (self.slug,), {}


class Images(models.Model):
    class Meta:
        ordering = ['sort']
        verbose_name = u'Изображения'
        verbose_name_plural = u'Изображения'

    image = ImageField(upload_to=get_file_path, verbose_name=u'Фото')
    product = models.ForeignKey('Product', null=True, blank=True, related_name='images')
    sort = models.IntegerField(default=0, verbose_name=u'Приоритет')

    def __unicode__(self):
        return u'Фото товара'
