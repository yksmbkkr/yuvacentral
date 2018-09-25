from django.conf.urls import include, url
from .views import home, login_redirect
from django.contrib.auth import views as auth_views


urlpatterns = [
    url(r'^$', home, name = 'home'),
    url(r'^login/login/$', auth_views.login, {'template_name': 'login.html'}, name='login'),
    url(r'^logout/$',auth_views.logout, {'next_page': 'landing:login'}, name = 'logout'),
    url(r'^login/$', login_redirect),
    ]
