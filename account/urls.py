from django.conf.urls import include, url
from django.contrib.auth import views as auth_views
from account import views as a_views


urlpatterns = [
    url(r'^template_test/$', a_views.template_test),
    url(r'^activate/(?P<uidb64>[0-9A-Za-z_\-]+)/(?P<token>[0-9A-Za-z]{1,13}-[0-9A-Za-z]{1,20})/$', a_views.activation, name = 'activate'),
    url(r'^register/$',a_views.register_yuva, name = 'register_yuva'),
    url(r'^profile/$',a_views.profile, name = 'profile'),
    url(r'^activation-status/$',a_views.activation_status, name = 're_activate'),
    url(r'^reactivate/$',a_views.create_reactivation, name = 'create_reactivation'),
]
