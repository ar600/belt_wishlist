from django.conf.urls import url
from . import views
urlpatterns = [
  url(r'^$', views.index),
  url(r'^register$', views.register),
  url(r'^login$', views.login),
  url(r'^home$', views.home),
  url(r'^new$', views.show_new),
  url(r'^add_new$', views.add_new),
  url(r'^logoff$', views.logoff) ,
  # url(r'^add_wish/(?P<id>\d+)$', views.add_wish) ,
  url(r'^remove/(?P<id>\d+)$', views.remove) ,
  url(r'^add/(?P<id>\d+)$', views.add) ,
  url(r'^delete/(?P<id>\d+)$', views.delete) ,

]
