from django.contrib import admin
from .models import *
from master.fields import AdminImageWidget, ThumbnailImageField


class CommentsInLine(admin.StackedInline):
    model = Comments
    extra = 0


class CategoriesAdmin(admin.ModelAdmin):
    list_display = ('category_id', 'category_name', 'in_header')
    list_display_links = ['category_name']
    list_editable = ['in_header']


class ArticlesAdmin(admin.ModelAdmin):
    search_fields = ('article_title', 'article_text')
    list_display = (
        'article_id', 'article_title', 'pic', 'article_date',
        'category_article_id', 'article_publish', 'recipe'
        )
    list_display_links = ('article_id', 'article_title')
    list_filter = ['category_article_id']
    list_editable = ('article_publish', 'recipe')
    formfield_overrides = {
        ThumbnailImageField: {'widget': AdminImageWidget},
    }
    inlines = [CommentsInLine]


class CommentsAdmin(admin.ModelAdmin):
    search_fields = ['comments_article']
    list_display = ['comment_date', 'user_name', 'comments_article', 'get_id']
    list_display_links = ['comment_date', 'user_name']
    list_filter = ['comment_date']


admin.site.register(Categories, CategoriesAdmin)
admin.site.register(Articles, ArticlesAdmin)
admin.site.register(Comments, CommentsAdmin)
