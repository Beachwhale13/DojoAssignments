from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.index),
    url(r'^register$',views.register),
    url(r'^login$',views.login),
    url(r'^logout$',views.logout),
    url(r'^add$',views.add),
    url(r'^books$',views.books),
    url(r'^process_add$',views.process_add),
    url(r'^user/(?P<number>\d+)$', views.show),
    url(r'^book/(?P<number>\d+)$', views.bookshow, name="showbook"),
    url(r'^addreview$', views.addreview),
    url(r'^delete/(?P<number>\d+)$', views.delete),

]
