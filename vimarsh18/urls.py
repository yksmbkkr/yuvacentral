from django.conf.urls import include, url
from vimarsh18 import views as v18_views
from django.contrib.auth import views as auth_views


urlpatterns = [
        url(r'^$',v18_views.vimarsh18_home, name = 'vimarsh18_home'),
        url(r'^volunteer-registration/$',v18_views.volunteer_registration, name = 'volunteer_reg'),
        url(r'^participant-registration/$',v18_views.participant_registration, name = 'participant_reg'),
        url(r'^volunteer-registration-profile-false/$',v18_views.volunteer_registration_false, name = 'volunteer_reg_false'),
        url(r'^participant-registration-profile-false/$',v18_views.participant_registration_false, name = 'participant_reg_false'),
        url(r'^pay-success/$',v18_views.payment_successful),
        url(r'^pay-failed/$',v18_views.payment_failed),
        url(r'^pay-pending/$',v18_views.payment_pending),
        url(r'^pay-reciept/$',v18_views.pay_reciept, name = 'pay_reciept'),
        url(r'^try/$',v18_views.idtry),
        url(r'^try/(?P<user_id>[\w]+)$',v18_views.idtry),
        url(r'^change-payment/$',v18_views.change_payment_mode, name = 'change_payment'),
        url(r'^session_api/$', v18_views.session_vimList.as_view()),
        url(r'^generate-all-id-participant/$',v18_views.all_participant_idcard),
        url(r'^generate-volunteer-general-id/$',v18_views.all_volunteer_idcard),
        url(r'^attendance/753864219/(?P<sid>[\w]+)/(?P<rid>[\w]+)$',v18_views.mark_attendance),
    ]
