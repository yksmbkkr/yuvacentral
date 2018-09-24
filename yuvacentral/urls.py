"""
Definition of urls for yuvacentral.
"""

from django.conf.urls import include, url
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.sitemaps.views import sitemap




# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()
from django.contrib.auth import views as auth_views

from .sitemaps import StaticViewSitemap

sitemaps = {
    'static': StaticViewSitemap,
}

urlpatterns = [
    # Examples:
    #url(r'^$', yuvacentral.views.home, name='home'),
    #url(r'^yuvacentral/', include('yuvacentral.yuvacentral.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),
    url(r'^', include('landing_page.urls', namespace = 'landing')),
    url(r'^account/', include('account.urls', namespace = 'account')),
    url(r'^vimarsh18/', include('vimarsh18.urls', namespace = 'vimarsh18')),
    url(r'^admin-dash/', include('manage_dashboard.urls', namespace = 'dashboard')),
    url(r'^password_reset/done/$', auth_views.password_reset_done, {'template_name':'password_reset_done.html'}, name='password_reset_done'),
    url(r'^reset/(?P<uidb64>[0-9A-Za-z_\-]+)/(?P<token>[0-9A-Za-z]{1,13}-[0-9A-Za-z]{1,20})/$',
        auth_views.password_reset_confirm, {'template_name':'password_reset_confirm.html'}, name='password_reset_confirm'),
    url(r'^reset/done/$', auth_views.password_reset_complete, {'template_name':'password_reset_complete.html'}, name='password_reset_complete'),
   
    url(r'^smap\.xml$', sitemap, {'sitemaps': sitemaps}, name='django.contrib.sitemaps.views.sitemap'),
]
#if settings.DEBUG:
#    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)