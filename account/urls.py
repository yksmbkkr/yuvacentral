from django.conf.urls import include, url
from django.contrib.auth import views as auth_views
from account import views as a_views


urlpatterns = [
    url(r'^template_test/$', a_views.template_test),
]
