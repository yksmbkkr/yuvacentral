from django.conf.urls import include, url
from django.contrib.auth import views as auth_views
from manage_dashboard import views as m_views


urlpatterns = [
    url(r'^template_test/$', m_views.template_test),
    url(r'^$', m_views.dash_home, name='dashboard_home'),
    url(r'^upcoming-events/$', m_views.add_upcoming_events, name='add_upcoming_events'),
    url(r'^upcoming-events/(?P<id>[\d]+)/$', m_views.add_upcoming_events, name='edit_event'),
    url(r'^list-upcoming-events/$', m_views.upcoming_events_list, name='list_upcoming_events'),
    url(r'^event-status/(?P<id>[\d]+)/(?P<status>[0-1])/$', m_views.make_event_live, name='event_status'),
    url(r'^add-manager/$', m_views.add_manager, name='add_manager'),
]
