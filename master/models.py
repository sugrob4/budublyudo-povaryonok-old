# -*- coding: utf-8 -*-
from django.db import models
from django.utils import timezone
import random
from ckeditor.fields import RichTextField
from ckeditor_uploader.fields import RichTextUploadingField
from django.conf import settings


def make_upload_path(instance, filename, prefix=False):
    n1 = random.randint(0, 10000)
    n2 = random.randint(0, 10000)
    n3 = random.randint(0, 10000)
    c = filename.split(".")
    filename = str(n1) + "_" + str(n2) + "_" + str(n3) + '.' + c[-1]
    return u"%s/%s" % (settings.IMAGE_UPLOAD_DIR, filename)


class Categories(models.Model):
    category_id = models.AutoField(primary_key=True, unique=True)
    category_name = models.CharField(max_length=200, db_index=True, unique=True, default='', verbose_name='Категория')
    metakey = models.CharField(max_length=255, blank=True, verbose_name='Ключевые слова')
    metadesc = models.CharField(max_length=255, blank=True, verbose_name='Мета описание')
    in_header = models.SmallIntegerField(default=0, blank=True, null=True, verbose_name='Категория в шапке сайта')
    class_in_header = models.CharField(max_length=20, default=False, blank=True, null=True)

    def __str__(self):
        return self.category_name

    class Meta:
        db_table = 'categories'
        verbose_name = 'категория'
        verbose_name_plural = 'категории'
        ordering = ['category_id']


class Articles(models.Model):
    article_id = models.AutoField(primary_key=True, unique=True)
    article_title = models.CharField(max_length=200, unique=True, blank=True, verbose_name='Заголовок статьи')
    metakey = models.CharField(max_length=255, blank=True, verbose_name='Ключевые слова')
    metadesc = models.CharField(max_length=255, blank=True, verbose_name='Мета описание')
    category_article = models.ForeignKey(Categories, blank=True, null=True, verbose_name="Категория статьи")
    image = models.ImageField(upload_to=make_upload_path, blank=True, verbose_name='Изображение')
    article_anons = RichTextField(blank=True, verbose_name='Анонс статьи')
    article_text = RichTextUploadingField(blank=True, verbose_name='Полный текст статьи')
    article_date = models.DateTimeField(default=timezone.now, blank=True, verbose_name="Дата публикации")
    recipe = models.BooleanField(default=False, verbose_name='Рецепт')
    article_publish = models.BooleanField(default=True, verbose_name="Опубликован")

    def __str__(self):
        return self.article_title

    def get_comment(self):
        return Comments.objects.filter(comments_article=self)

    def pic(self):
        if self.image:
            return u'<img src="%s" width="70" />' % self.image.url
        else:
            return '(none)'
    pic.short_description = u'Большая картинка'
    pic.allow_tags = True

    class Meta:
        db_table = 'articles'
        verbose_name = 'Статья, рецепт'
        verbose_name_plural = 'Статьи и рецепты'


class Comments(models.Model):
    comment_id = models.AutoField(primary_key=True, unique=True)
    user_name = models.CharField(max_length=50, verbose_name='Имя пользователя')
    comment_date = models.DateField(default=timezone.now, verbose_name='Дата')
    comments_text = models.TextField(blank=True, verbose_name='Кометарий')
    comments_article = models.ForeignKey(Articles, blank=True, null=True, related_name='com', verbose_name='Коментарий для статьи')

    def __str__(self):
        return self.user_name

    def get_id(self):
        return self.comments_article_id
    get_id.short_description = u'ID Статьи'

    class Meta:
        db_table = "comments"
        verbose_name = "коментарий"
        verbose_name_plural = "коментарии"
        ordering = ['-comment_date']
