from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.buffet_list, name='buffet_list'),
]