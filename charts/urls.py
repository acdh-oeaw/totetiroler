from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^barcharts/$', views.barcharts_view, name='bar_charts'),
    url(r'^testjson/$', views.test_json, name='test_json'),
    url(r'^piecharts/$', views.piecharts_view, name='pie_charts'),
    url(r'^testjsonpie/$', views.test_json_pie, name='test_json_pie'),
    url(r'^professions/$', views.death_by_profession, name='professions'),
    url(r'^deaths/$', views.death_by_death, name='deaths'),
]
