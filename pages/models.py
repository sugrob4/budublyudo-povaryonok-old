# -*- coding: utf-8 -*-
from django.db import models
from ckeditor_uploader.fields import RichTextUploadingField


class Pages(models.Model):
    page_id = models.AutoField(primary_key=True, unique=True)
    title = models.CharField(max_length=200, unique=True, blank=True, verbose_name='Страница')
    metakey = models.CharField(max_length=255, blank=True, verbose_name='Ключевые слова')
    metadesc = models.CharField(max_length=255, blank=True, verbose_name='Мета описание')
    slug = models.CharField(max_length=250, blank=True, verbose_name="Урл")
    page_text = RichTextUploadingField(blank=True, verbose_name='Текст страницы')
    position = models.SmallIntegerField(verbose_name='Позиция')

    def get_url(self):
        return "/%s/" % self.slug

    def __str__(self):
        return self.title

    class Meta:
        db_table = 'pages'
        verbose_name = 'страница'
        verbose_name_plural = 'страницы'
        ordering = ['position']
