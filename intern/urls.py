from django.urls import include, path, re_path
from intern import views
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    re_path(r'^$',views.intern_home, name = 'home'),
    #re_path(r'^register/$',views.intern_field, name = 'register'),
    #re_path(r'^register/(.{1,10})/$',views.intern_register),
    re_path(r'^apply/(.{1,7})/$',views.apply_intern),
    re_path(r'^download/$', views.pdf_download, name= 'download' ),
    re_path(r'^additional_data/$', views.create_profile, name= 'create_profile' ),
    #re_path(r'^trial/$',views.trial),
    re_path(r'^user_list/$',views.view_reg, name = 'user_list'),
    re_path(r'^download_list/$',views.download_list, name = 'download_list'),
    re_path(r'^resume_download/(.{1,150})/$',views.resume_download),
    ]

# if settings.DEBUG:
#     urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)