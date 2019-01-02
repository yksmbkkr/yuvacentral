from django.urls import include, path, re_path
from vimarsh18 import views as v18_views
from django.contrib.auth import views as auth_views



urlpatterns = [
        re_path(r'^$',v18_views.vimarsh18_home, name = 'vimarsh18_home'),
        re_path(r'^volunteer-registration/$',v18_views.volunteer_registration, name = 'volunteer_reg'),
        re_path(r'^participant-registration/$',v18_views.participant_registration, name = 'participant_reg'),
        re_path(r'^volunteer-registration-profile-false/$',v18_views.volunteer_registration_false, name = 'volunteer_reg_false'),
        re_path(r'^participant-registration-profile-false/$',v18_views.participant_registration_false, name = 'participant_reg_false'),
        re_path(r'^pay-success/$',v18_views.payment_successful),
        re_path(r'^pay-failed/$',v18_views.payment_failed),
        re_path(r'^pay-pending/$',v18_views.payment_pending),
        re_path(r'^pay-reciept/$',v18_views.pay_reciept, name = 'pay_reciept'),
        re_path(r'^try/$',v18_views.idtry),
        re_path(r'^try/(?P<user_id>[\w]+)$',v18_views.idtry),
        re_path(r'^change-payment/$',v18_views.change_payment_mode, name = 'change_payment'),
        re_path(r'^session_api/$', v18_views.session_vimList.as_view()),
        re_path(r'^generate-all-id-participant/$',v18_views.all_participant_idcard),
        re_path(r'^generate-volunteer-general-id/$',v18_views.all_volunteer_idcard),
        re_path(r'^attendance/753864219/(?P<sid>[\w]+)/(?P<rid>[\w]+)$',v18_views.mark_attendance),
        re_path(r'^download-schedule/$', v18_views.schedule_download, name="download_schedule"),
        re_path(r'^request-certificate-hardcopy/$',v18_views.hardcopy_request, name = 'hardcopy_request'),
        re_path(r'^feedback/$', v18_views.feedback, name="feedback"),
        re_path(r'^volunteer-certificate/$', v18_views.certi_volunteer_request, name="v_certi"),
    ]
