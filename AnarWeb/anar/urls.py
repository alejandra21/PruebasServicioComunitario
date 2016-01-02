from django.conf.urls import patterns, include, url
from django.conf import settings
# Uncomment the next two lines to enable the admin:
from django.contrib import admin
import os


admin.autodiscover()

urlpatterns = patterns('',
	# Examples:
	# url(r'^$', 'anar.views.home', name='home'),
	# url(r'^anar/', include('anar.foo.urls')),
	# url(r'^yacimientos/$', 'anarapp.views.index'),
	# url(r'^mapa/$', 'geoespacial.views.mapa'),
	url(r'^', include('anarapp.urls')),
	url(r'^upload/(?P<path>.*)$','django.views.static.serve',
		{'document_root':settings.MEDIA_ROOT,}
	),

	url(r'^static/(.*)$', 'django.views.static.serve', {'document_root':           
    os.path.join(os.path.dirname(__file__), 'static')}),

	# Uncomment the admin/doc line below to enable admin documentation:
	url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

	# Uncomment the next line to enable the admin:        
	url(r'^admin/', include(admin.site.urls)),

	# Incluyendo los smarts selects
	url(r'^chaining/', include('smart_selects.urls')),
		
	# Incluyendo los cruces
	url(r'^cruces/', include('joins.urls')),

)