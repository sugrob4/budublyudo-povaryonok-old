from django.conf.urls import url, include
from django.contrib import admin
from django.conf.urls.static import static
from django.conf import settings
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
import master
import pages
from master import views
from pages import views
from django.contrib.sitemaps.views import sitemap
from povaryonok.utils.sitemap import *

sitemaps = {
    'articles': ArticleSitemap, 'static': PagesSitemap, 'categoryes': CategorySitemap
}

urlpatterns = [
    url(r'^$', master.views.home, name="home"),
    url(r'^cat/([\d]+)/$', master.views.categories, name="cat"),
    url(r'^article/([\d]+)?/$', master.views.view_detailed, name="article"),
    url(r'^addcomment/([\d]+)/$', master.views.addcomment, name="addcomment"),
    url(r'^recipes/$', pages.views.recipes_page, name="recipes"),
    url(r'^registration/$', master.views.registration, name="registration"),
    url(r'^contacts/$', pages.views.contacts, name="contacts"),
    url(r'^sitemap/$', pages.views.sitemap, name="sitemap"),
    url(r'^aboutsite/$', pages.views.aboutsite, name="aboutsite"),
    url(r'^search/$', pages.views.search, name="search"),
    url(r'^', include('loginsys.urls')),
    url(r'^sitemap\.xml$', sitemap, {'sitemaps': sitemaps},
        name='django.contrib.sitemaps.views.sitemap'),
    url(r'^robots\.txt', master.views.robots),
    url(r'^dublin\.rdf', master.views.dublin),
    url(r'^povaryonok_admin_ZRehf534Szez/', admin.site.urls),
    url(r'^povaryonok_admin_ZRehf534Szez/', include('manager_files.urls')),
    url(r'^ckeditor/', include('ckeditor_uploader.urls')),
]+static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
urlpatterns += static(settings.MEDIA_URL, documnet_root=settings.MEDIA_ROOT)
urlpatterns += staticfiles_urlpatterns()
