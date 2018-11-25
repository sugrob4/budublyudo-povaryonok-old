# -*- coding: utf-8 -*-
from django.contrib.sitemaps import Sitemap
from master.models import Articles, Categories
from django.core.urlresolvers import reverse


class ArticleSitemap(Sitemap):
    changefreq = "daily"
    priority = 0.5

    def items(self):
        return Articles.objects.filter(article_publish=True)

    def lastmod(self, article):
        return article.article_date

    def location(self, article):
        return "/article/" + format(article.article_id) + format("/")


class CategorySitemap(Sitemap):
    changefreq = "daily"
    priority = 0.5

    def items(self):
        return Categories.objects.all()

    def location(self, obj):
        return "/cat/" + format(obj.category_id) + format("/")


class PagesSitemap(Sitemap):
    changefreq = "weekly"
    priority = 0.5

    def items(self):
        if '/':
            home = 'home'
            return [home, 'recipes', 'contacts', 'sitemap', 'aboutsite']

    def location(self, obj):
        return reverse(obj)
