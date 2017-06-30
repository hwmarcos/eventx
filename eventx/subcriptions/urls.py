from django.conf.urls import url
from eventx.subcriptions.views import new, detail

urlpatterns = [
    url(r'^$', new, name='new'),
    url(r'^(?P<pk>\d+)/$', detail, name='detail'),
]