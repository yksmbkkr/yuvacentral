from django.contrib import admin
from vimarsh18.models import *

# Register your models here.

@admin.register(volunteer)
class volunteerAdmin(admin.ModelAdmin):
    list_display = ('get_usrname', 'reg_no', 'interest')
    list_filter = ('interest',)
    search_fields = ('user__username', 'reg_no')
    def get_usrname(self, obj):
        return obj.user.username

#admin.site.register(volunteer, volunteerAdmin)
@admin.register(participant)
class participantAdmin(admin.ModelAdmin):
    list_display = ('get_usrname', 'reg_no', 'pay_mode', 'payment_status',)
    list_filter = ('pay_mode', 'payment_status')
    search_fields = ('user__username', 'reg_no')
    def get_usrname(self, obj):
        return obj.user.username