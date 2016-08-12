# -*- coding: utf-8 -*-
from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^list/$', views.PersonListView.as_view(), name='person_list'),
    url(
        r'^detail/(?P<pk>[0-9]+)$', views.PersonDetailView.as_view(),
        name='person_detail'),
]
