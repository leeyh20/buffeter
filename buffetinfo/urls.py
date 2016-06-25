from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.buffet_list, name='buffet_list'),
    url(r'^buffet/(?P<pk>\d+)/$', views.buffet_detail, name = 'buffet_detail'),
    url(r'^buffet/new/$', views.buffet_new, name='buffet_new'),
    url(r'^buffet/(?P<pk>\d+)/edit/$', views.buffet_edit, name='buffet_edit'),
    url(r'^drafts/$', views.buffet_draft_list, name='buffet_draft_list'),
    url(r'^buffet/(?P<pk>\d+)/publish/$', views.buffet_publish, name='buffet_publish'),
    url(r'^buffet/(?P<pk>\d+)/remove/$', views.buffet_remove, name='buffet_remove'),
]