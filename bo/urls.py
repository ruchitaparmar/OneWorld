from django.conf.urls import url
from . import views


urlpatterns = [url(r'^bo/$', views.dashboard, name='dashboard'),
               # url(r'^profile/$', views.profile, name='profile')
               ]
