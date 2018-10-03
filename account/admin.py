from django.contrib import admin
from account import models as a_models

# Register your models here.

@admin.register(a_models.user_check)
class user_checkAdmin(admin.ModelAdmin):
    list_display = ('user_username', 'email_confirmation_status', 'profile_status', 'manager_status', 'reciept_manager_status', 'profession')
    list_filter = ('email_confirmation_status', 'profile_status', 'manager_status', 'reciept_manager_status', 'profession')
    search_fields = ('user__username',)
    def user_username(self,obj):
        return obj.user.username

@admin.register(a_models.profile)
class profileAdmin(admin.ModelAdmin):
    list_display = ('user_username', 'name')
    search_fields = ('user__username','name')
    def user_username(self,obj):
        return obj.user.username

@admin.register(a_models.college_list_yuva)
class college_list_yuva(admin.ModelAdmin):
    search_fields = ('college_name',)