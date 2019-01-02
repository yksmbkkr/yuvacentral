from django.urls import include, path, re_path
from django.contrib.auth import views as auth_views
from account import views as a_views

urlpatterns = [
    re_path(r'^template_test/$', a_views.template_test),
    re_path(r'^activate/(?P<uidb64>[0-9A-Za-z_\-]+)/(?P<token>[0-9A-Za-z]{1,13}-[0-9A-Za-z]{1,20})/$', a_views.activation, name = 'activate'),
    re_path(r'^register/$',a_views.register_yuva, name = 'register_yuva'),
    re_path(r'^profile/$',a_views.profile, name = 'profile'),
    re_path(r'^activities/$',a_views.activities, name = 'activities'),
    re_path(r'^forgot-password/$',a_views.forgot_password, name = 'forgot_password'),
    re_path(r'^activation-status/$',a_views.activation_status, name = 're_activate'),
    re_path(r'^reactivate/$',a_views.create_reactivation, name = 'create_reactivation'),
    re_path(r'^update-email/$',a_views.change_mail, name = 'update_email'),
    re_path(r'^password_reset/done/$', auth_views.PasswordResetDoneView.as_view(template_name = 'password_reset_done.html'), name='password_reset_done'),
    re_path(r'^reset/(?P<uidb64>[0-9A-Za-z_\-]+)/(?P<token>[0-9A-Za-z]{1,13}-[0-9A-Za-z]{1,20})/$',
        auth_views.PasswordResetConfirmView.as_view(template_name='password_reset_confirm.html'), name='password_reset_confirm'),
    re_path(r'^reset/done/$', auth_views.PasswordResetCompleteView.as_view(template_name='password_reset_complete.html'), name='password_reset_complete'),
    re_path(r'^modify-password/$',a_views.change_password, name = 'change_password'),
]
