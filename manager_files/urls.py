# -*- coding: utf-8 -*-
from django.conf.urls import url
from manager_files import views


urlpatterns = [
    url(r'image_browser/$', views.image_browser, name='image_browser'),
    url(r'image_uploader/$', views.image_uploader, name='image_uploader'),
]
