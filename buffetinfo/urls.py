from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.buffet_list, name='buffet_list'),
    url(r'^buffet/(?P<pk>\d+)/$', views.buffet_detail, name = 'buffet_detail'),
    url(r'^buffet/new/$', views.buffet_new, name='buffet_new'),
]