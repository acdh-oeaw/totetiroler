from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'persons/$', views.PersonListView.as_view(), name='browse_persons'),
    url(r'^persons/show/$', views.LocatePersons.as_view(), name='person_map'),
]
