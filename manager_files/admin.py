# -*- coding: utf-8 -*-
from django.contrib import admin
from manager_files.models import Upload


class UploadAdmin(admin.ModelAdmin):
    list_display = ('image_tag', 'pic', 'add_date', 'height', 'width', 'remove')
    list_filter = ['add_date']
    search_fields = ['image']

admin.site.register(Upload, UploadAdmin)
