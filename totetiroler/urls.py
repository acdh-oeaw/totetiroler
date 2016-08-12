from django.conf.urls import url, include
from django.contrib import admin

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^', include('webpage.urls', namespace='webpage')),
    url(r'^account/', include('account.urls', namespace='account')),
    url(r'^places/', include('places.urls', namespace='places')),
    url(r'^persons/', include('persons.urls', namespace='persons')),
    url(r'^datamodel/', include('django_spaghetti.urls', namespace='datamodel')),
    url(r'^browsing/', include('browsing.urls', namespace='browsing')),
    url(r'^charts/', include('charts.urls', namespace='charts')),
]
