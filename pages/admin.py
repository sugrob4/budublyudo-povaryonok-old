from django.contrib import admin
from .models import Pages


class PagesAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ("title",)}
    list_display = ('page_id', 'title', 'position', 'slug')
    list_display_links = ['title']
    list_editable = ['position', 'slug']


admin.site.register(Pages, PagesAdmin)
