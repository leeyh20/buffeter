from django.conf.urls import url
from django.contrib.auth.views import login
from django.contrib.auth.views import logout
from . import views

urlpatterns = [
    url(r'^login/$', login, name='login'),
    url(r'^logout/$', logout, name='logout', kwargs={'next_page': '/'}),
    url(r'^new/$', views.account_new, name="account_new"),
]