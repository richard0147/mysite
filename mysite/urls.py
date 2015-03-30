from django.conf.urls import patterns, include, url
from django.contrib import admin

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'mysite.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    
    url(r'^polls/', include('polls.urls', namespace="polls")),
    url(r'^reports/', include('reports.urls', namespace="reports")),
    url(r'^admin/', include(admin.site.urls)),
)

#media files
urlpatterns += patterns('',  
      url(r'^media/(?P<path>.*)','django.views.static.serve',{'document_root':'/home/richard/develop/mysite/media'}),  
)