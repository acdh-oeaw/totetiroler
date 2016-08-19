from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.start_view, name="start"),
    # following url is needed to keep legacy links to this app alive
    url(r'^totetiroler/$', views.start_view, name='start'),
    url(r'^imprint/$', views.imprint_view, name='imprint'),
    url(r'^about/$', views.about_view, name='about'),
]
