from django.contrib import admin

# Register your models here.

from manage_dashboard import models as m_models

admin.site.register(m_models.up_events)
