from django.urls import include, path, re_path
from .views import home, login_redirect, vimarsh_redirect, privacy_policy
from django.contrib.auth import views as auth_views



urlpatterns = [
    re_path(r'^$', home, name = 'home'),
    re_path(r'^login/login/$', auth_views.LoginView.as_view(template_name='login.html'), name='login'),
    re_path(r'^logout/$',auth_views.LogoutView.as_view(next_page = 'landing:login'),  name = 'logout'),
    re_path(r'^login/$', login_redirect),
    re_path(r'^vimarsh/$', vimarsh_redirect),
    re_path(r'^privacy-policy/$',privacy_policy, name = 'privacy_policy'),

    ]
