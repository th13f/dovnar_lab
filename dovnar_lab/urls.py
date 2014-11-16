from django.conf import settings
from django.conf.urls import patterns, include, url

from django.contrib import admin
from django.conf.urls.static import static

admin.autodiscover()

urlpatterns = patterns('base.views',
                       # Examples:
                       # url(r'^$', 'dovnar_lab.views.home', name='home'),
                       # url(r'^blog/', include('blog.urls')),
                       #url(r'^grappelli/', include('grappelli.urls')),  # grappelli URLS
                       url(r'^admin/', include(admin.site.urls)),

                       url(r'^/?$', 'index', name='index'),

                       url(r'^get_third_table/?$', 'get_third_table', name='get_third_table'),
                       url(r'^get_tablice_html/?$', 'get_tablice_html', name='get_tablice_html'),
                       url(r'^get_tablice_json/?$', 'get_tablice_json', name='get_tablice_json'),

                       # reports api
                       url(r'^reports_list/?$', 'reports_list', name='reports_list'),
                       url(r'^save_report/(?P<report_name>.+)/?$', 'save_report', name='save_report'),
                       url(r'^update_report/(?P<report_id>\d+)/?$', 'update_report', name='update_report'),
                       url(r'^delete_report/(?P<report_id>\d+)/?$', 'delete_report', name='delete_report'),
                       url(r'^load_report/(?P<report_id>\d+)/?$', 'load_report', name='load_report'),
                       url(r'^download_report/(?P<report_id>\d+)/?$', 'download_report', name='download_report'),


)

urlpatterns += patterns('', url(r'^media/(?P<path>.*)$',
                                'django.views.static.serve', {'document_root': settings.MEDIA_ROOT, })
)
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

