from django.conf.urls import url, include
from django.contrib import admin
from . import views


urlpatterns = [
    url(r'^$', views.base , name="base"),
    url(r'^login$', views.login , name="login"),
    url(r'^home$', views.home , name="home"),
    url(r'^signup$', views.signup , name="signup"),
]
