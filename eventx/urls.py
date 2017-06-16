from django.conf.urls import include, url
from django.contrib import admin
from eventx.core.views import home

urlpatterns = [
    url(r'^$', home, name='home'),
    url(r'inscricao/', include('eventx.subcriptions.urls', namespace='subscriptions')),
    url(r'^admin/', include(admin.site.urls)),
]