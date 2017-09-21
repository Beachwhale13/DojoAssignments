from django.conf.urls import url
import views

urlpatterns = [
    url(r'^$', views.display),
    url(r'^users/$', views.display),
    url(r'^register$', views.register),
    url(r'^login$', views.login),
    url(r'^new$', views.register),
]
