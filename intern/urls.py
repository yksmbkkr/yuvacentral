from django.conf.urls import include, url
from intern import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    url(r'^$',views.intern_home, name = 'home'),
    #url(r'^register/$',views.intern_field, name = 'register'),
    #url(r'^register/(.{1,10})/$',views.intern_register),
    url(r'^apply/(.{1,7})/$',views.apply_intern),
    url(r'^download/$', views.pdf_download, name= 'download' ),
    url(r'^additional_data/$', views.create_profile, name= 'create_profile' ),
    #url(r'^trial/$',views.trial),
    url(r'^user_list/$',views.view_reg, name = 'user_list'),
    url(r'^download_list/$',views.download_list, name = 'download_list'),
    url(r'^resume_download/(.{1,150})/$',views.resume_download),
    ]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)