# -*- coding: utf-8 -*-
from django.db import models
from django.utils.translation import ugettext_lazy as _
from manager_files.utils import UploadPath
from django.db.models.signals import pre_delete
from manager_files.signals import delete_file


class Upload(models.Model):
    path = UploadPath('uploads')
    image = models.ImageField(_('Image'), upload_to=path, height_field='height', width_field='width')
    height = models.PositiveIntegerField(null=True, blank=True, editable=False, default="100", verbose_name='Высота')
    width = models.PositiveIntegerField(null=True, blank=True, editable=False, default="100", verbose_name='Ширина')
    add_date = models.DateTimeField(_('Дата добавления'), auto_now_add=True)

    def __str__(self):
        return self.image.name

    def image_tag(self):
        return format(self.image.url)

    image_tag.short_description = _('Предварительный просмотр')
    image_tag.allows_tags = True

    def remove(self):
        return '<input type="button" class="btn-info btn" value="Удалить" onclick="location.href=\'%s/delete/\'" />' % (self.pk)

    remove.short_description = _('Удаление изображения')
    remove.allow_tags = True

    def pic(self):
        return u'<img src="%s" width="70" />' % self.image_tag()

    pic.short_description = u'Изображение'
    pic.allow_tags = True

pre_delete.connect(delete_file, sender=Upload)
