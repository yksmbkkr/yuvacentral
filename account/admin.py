from django.contrib import admin
from account import models as a_models

# Register your models here.

admin.site.register(a_models.user_check)
admin.site.register(a_models.profile)
admin.site.register(a_models.college_list_yuva)