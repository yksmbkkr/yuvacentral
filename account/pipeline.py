from django.contrib.auth.models import User
from account.models import *
from django.contrib import messages

def add_email(backend, user, response, *args, **kwargs):
    if backend.name == 'facebook' and user_check.objects.filter(user=user).count() < 1:
       user_obj = User.objects.get(id=user.id)
       user_obj.email = str(response.get('email'))
       user_obj.save()

    if user_check.objects.filter(user=user).count() < 1:
        user_check_obj = user_check(user=user, email_confirmation_status = True)
        user_check_obj.save()
    #    profile = user.get_profile()
    #    if profile is None:
    #        profile = Profile(user_id=user.id)
    #    profile.gender = response.get('gender')
    #    profile.link = response.get('link')
    #    profile.timezone = response.get('timezone')
    #    profile.save()
