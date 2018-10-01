from django.conf.urls import include, url
from vimarsh18 import views as v18_views
from django.contrib.auth import views as auth_views


urlpatterns = [
        url(r'^volunteer-registration/$',v18_views.volunteer_registration, name = 'volunteer_reg'),
        url(r'^volunteer-registration-profile-false/$',v18_views.volunteer_registration_false, name = 'volunteer_reg_false'),
        url(r'^pay-success/$',v18_views.payment_successful),
        url(r'^pay-failed/$',v18_views.payment_failed),
        url(r'^pay-pending/$',v18_views.payment_pending),
    ]
