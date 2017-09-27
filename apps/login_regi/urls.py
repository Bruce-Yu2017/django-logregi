from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.index),
    url(r'^regi', views.regi),
    url(r'^login$', views.login),
    url(r'^success$', views.success)
]
