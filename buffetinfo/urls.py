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
    #url(r'^filter/location/(?P<pk>[\w\ ]+)/$', views.buffet_filter_location, name='buffet_filter_location'),
    url(r'^buffet/(?P<pk>\d+)/review/$', views.add_review_to_buffet, name='add_review_to_buffet'),
    url(r'^review/(?P<pk>\d+)/approve/$', views.review_approve, name='review_approve'),
	url(r'^review/(?P<pk>\d+)/remove/$', views.review_remove, name='review_remove'),
    
]