from django.urls import include, path, re_path
from django.contrib.auth import views as auth_views
from manage_dashboard import views as m_views

urlpatterns = [
    re_path(r'^template_test/$', m_views.template_test),
    re_path(r'^$', m_views.dash_home, name='dashboard_home'),
    re_path(r'^upcoming-events/$', m_views.add_upcoming_events, name='add_upcoming_events'),
    re_path(r'^speaker/$', m_views.speaker, name='speaker'),
    re_path(r'^speaker/(?P<id>[\d]+)/$', m_views.speaker, name='edit_speaker'),
    re_path(r'^upcoming-events/(?P<id>[\d]+)/$', m_views.add_upcoming_events, name='edit_event'),
    re_path(r'^list-upcoming-events/$', m_views.upcoming_events_list, name='list_upcoming_events'),
    re_path(r'^vimarsh-session/$', m_views.session_vim, name='session_vim'),
    re_path(r'^vimarsh-session/(?P<id>[\d]+)/$', m_views.session_vim, name='edit_session_vim'),
    re_path(r'^event-status/(?P<id>[\d]+)/(?P<status>[0-1])/$', m_views.make_event_live, name='event_status'),
    re_path(r'^add-manager/$', m_views.add_manager, name='add_manager'),
    re_path(r'^add-recipt-manager/$', m_views.add_reciept_manager, name='add_reciept_manager'),
    re_path(r'^generate-reciept/$', m_views.generate_reciept, name='generate_reciept'),
    re_path(r'^vimarsh-volunteer-list/$', m_views.volunteer_list, name='vv_list'),
    re_path(r'^vimarsh-participant-list/$', m_views.participant_list, name='p_list'),
    re_path(r'^vimarsh-reciept-manager-list/$', m_views.reciept_manager_list, name='rm_list'),
    re_path(r'^vimarsh-reciept-list/$', m_views.reciept_list, name='r_list'),
    re_path(r'^non-participant-profile/$', m_views.get_non_participant_list, name='nplist'),
    re_path(r'^online-payment-confirmation/$', m_views.online_payment_confirmation, name='online_payment_confirmation'),
    re_path(r'^offline-payment/$', m_views.offline_payment, name='offline_payment'),
    re_path(r'^id-generator/$', m_views.id_creator, name='id_special'),
]
