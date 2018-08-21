from django.conf.urls import include, url
from django.contrib.auth import views as auth_views
from manage_dashboard import views as m_views


urlpatterns = [
    url(r'^template_test/$', m_views.template_test),
    url(r'^add-upcoming-events/$', m_views.add_upcoming_events, name='add_upcoming_events'),
]
