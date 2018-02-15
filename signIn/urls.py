from django.conf.urls import url
from . import views


urlpatterns = [url(r'^register/$', views.register, name='register'),
               url(r'^$', views.home, name='home'),
               url(r'^menu/$', views.menu, name='menu'),
               url(r'^donorPage/$', views.donorPage, name='donorPage')
               ]
