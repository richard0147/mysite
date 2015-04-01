from django.conf.urls import patterns, url
from reports import views

urlpatterns = patterns('',
    # ex: /reports/
    url(r'^$', views.index, name='index'),
    # ex: /reports/create/
    url(r'^create/$', views.create, name='create'),
    # ex: /reports/5/view/
    url(r'^(?P<report_id>\d+)/view/$', views.view, name='view'),
    # ex: /reports/5/detail/
    url(r'^new/$', views.new, name='new'),
    
    url(r'^sendmail/$', views.sendmail, name='sendmail'),
)
