from django.contrib import admin

# Register your models here.

from manage_dashboard import models as m_models

admin.site.register(m_models.up_events)
@admin.register(m_models.vimarsh18_reciept)
class vimarsh18_recieptAdmin(admin.ModelAdmin):
    list_display = ('number', 'status', 'creator_username')
    list_filter = ('status',)
    search_fields = ('number', 'creator__username')
    def creator_username(self,obj):
        return obj.creator.username