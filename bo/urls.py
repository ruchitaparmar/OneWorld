from django.conf.urls import url
from . import views


urlpatterns = [url(r'^dashboard/$', views.dashboard, name='dashboard'),
               url(r'^addRefugee/$', views.addRefugee, name='addRefugee'),
               url(r'^addShelter/$', views.addShelter, name='addShelter'),
               url(r'^showRefugee/$', views.showRefugee, name='showRefugee'),
               url(r'^showShelter/$', views.showShelter, name='showShelter'),
               url(r'^refugeeCard/$', views.refugeeCard, name='refugeeCard'),
               url(r'^shelterCard/$', views.shelterCard, name='shelterCard'),
               url(r'^search/$', views.search, name='search')
               ]
