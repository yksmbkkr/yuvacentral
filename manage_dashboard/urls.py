from django.conf.urls import include, url
from django.contrib.auth import views as auth_views
from manage_dashboard import views as m_views


urlpatterns = [
    url(r'^template_test/$', m_views.template_test),
    url(r'^$', m_views.dash_home, name='dashboard_home'),
    url(r'^upcoming-events/$', m_views.add_upcoming_events, name='add_upcoming_events'),
    url(r'^speaker/$', m_views.speaker, name='speaker'),
    url(r'^speaker/(?P<id>[\d]+)/$', m_views.speaker, name='edit_speaker'),
    url(r'^upcoming-events/(?P<id>[\d]+)/$', m_views.add_upcoming_events, name='edit_event'),
    url(r'^list-upcoming-events/$', m_views.upcoming_events_list, name='list_upcoming_events'),
    url(r'^vimarsh-session/$', m_views.session_vim, name='session_vim'),
    url(r'^vimarsh-session/(?P<id>[\d]+)/$', m_views.session_vim, name='edit_session_vim'),
    url(r'^event-status/(?P<id>[\d]+)/(?P<status>[0-1])/$', m_views.make_event_live, name='event_status'),
    url(r'^add-manager/$', m_views.add_manager, name='add_manager'),
    url(r'^add-recipt-manager/$', m_views.add_reciept_manager, name='add_reciept_manager'),
    url(r'^generate-reciept/$', m_views.generate_reciept, name='generate_reciept'),
    url(r'^vimarsh-volunteer-list/$', m_views.volunteer_list, name='vv_list'),
    url(r'^vimarsh-participant-list/$', m_views.participant_list, name='p_list'),
    url(r'^vimarsh-reciept-manager-list/$', m_views.reciept_manager_list, name='rm_list'),
    url(r'^vimarsh-reciept-list/$', m_views.reciept_list, name='r_list'),
    url(r'^online-payment-confirmation/$', m_views.online_payment_confirmation, name='online_payment_confirmation'),
]
