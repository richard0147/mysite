from django.conf.urls import patterns, url
from reports import views

urlpatterns = patterns('',
    # ex: /reports/
    url(r'^$', views.index, name='index'),
    # ex: /reports/create/
    url(r'^create/$', views.create, name='create'),
    # ex: /reports/5/view/
    url(r'^(?P<report_id>\d+)/view/$', views.view, name='view'),
    
    url(r'^(?P<report_id>\d+)/change/$', views.change, name='change'),
    # ex: /reports/5/detail/
    
    url(r'^sendmail/$', views.sendmail, name='sendmail'),
    url(r'^getDnslaCurrentData/$', views.getDnslaCurrentData, name='getDnslaCurrentData'),
)
