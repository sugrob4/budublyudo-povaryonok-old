from django.conf.urls import url
from loginsys import views

urlpatterns = [
    url(r'^login/', views.login_user, name="login_user"),
    url(r'^logout/$', views.logout_user, name="logout_user"),
    url(r'^register/$', views.register, name="register"),
]
