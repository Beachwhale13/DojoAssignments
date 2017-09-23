from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.index),
    url(r'^new/', views.adduser),
    url(r'^process$', views.process),
    url(r'^(?P<number>\d+)$', views.show),
    url(r'^(?P<number>\d+)/edit$', views.edit),
    url(r'^edit$', views.update),
    url(r'^(?P<number>\d+)/delete$', views.delete),
]
