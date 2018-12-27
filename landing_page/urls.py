from django.conf.urls import include, url
from .views import home, login_redirect, vimarsh_redirect, privacy_policy
from django.contrib.auth import views as auth_views


urlpatterns = [
    url(r'^$', home, name = 'home'),
    url(r'^login/login/$', auth_views.login, {'template_name': 'login.html'}, name='login'),
    url(r'^logout/$',auth_views.logout, {'next_page': 'landing:login'}, name = 'logout'),
    url(r'^login/$', login_redirect),
    url(r'^vimarsh/$', vimarsh_redirect),
   url(r'^privacy-policy/$',privacy_policy, name = 'privacy_policy'),

    ]
