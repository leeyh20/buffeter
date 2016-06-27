from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^new/$', views.account_new, name="account_new"),
]