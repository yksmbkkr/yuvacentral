"""
Definition of urls for yuvacentral.
"""

from django.urls import include, path, re_path
from django.conf import settings
from django.conf.urls.static import static

from django.contrib.sitemaps.views import sitemap
#from django.contrib import sitemaps as smap

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
    path('admin/', admin.site.urls),
    path('', include(('landing_page.urls', 'landing'), namespace='landing')),
    path('account/', include(('account.urls', 'account'), namespace='account')),
    path('vimarsh18/', include(('vimarsh18.urls', 'vimarsh18'), namespace='vimarsh18')),
    path('admin-dash/', include(('manage_dashboard.urls', 'manage_dashboard'), namespace='dashboard')),
    path(r'intern/', include(('intern.urls','intern'), namespace = 'intern')),
    path(r'oauth/', include(('social_django.urls', 'social'), namespace='social')),
    path('password_reset/done/', auth_views.PasswordResetDoneView.as_view(template_name= 'password_reset_done.html'),
        name='password_reset_done'),
    re_path(r'^reset/(?P<uidb64>[0-9A-Za-z_\-]+)/(?P<token>[0-9A-Za-z]{1,13}-[0-9A-Za-z]{1,20})/$',
        auth_views.PasswordResetConfirmView.as_view(template_name= 'password_reset_confirm.html'),
        name='password_reset_confirm'),
    re_path(r'^reset/done/$', auth_views.PasswordResetCompleteView.as_view(template_name= 'password_reset_complete.html'),
        name='password_reset_complete'),
    #url('', include('pwa.urls')),
    re_path(r'^sitemap\.xml$', sitemap, {'sitemaps': sitemaps}, name='django.contrib.sitemaps.views.sitemap'),
]
# if settings.DEBUG:
#     urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
#     urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)