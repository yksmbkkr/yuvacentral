from account import models as a_models
from django.contrib import messages
from django.shortcuts import redirect
from django.contrib.auth import logout

def is_profile_created(f):
    def wrap(request, *args, **kwargs):
        profile_object = a_models.user_check.objects.get(user = request.user)
        if not profile_object.email_confirmation_status:
            return redirect('account:re_activate')
        elif not profile_object.profile_status:
            messages.warning(request,"Complete your profile first")
            return redirect('account:profile')
        return f(request, *args, **kwargs)

    wrap.__doc__ = f.__doc__
    wrap.__name__=f.__name__
    return wrap

def is_confirm_mail(f):
    def wrap(request, *args, **kwargs):
        email_confirmation_object = a_models.user_check.objects.get(user = request.user)
        if not email_confirmation_object.email_confirmation_status:
            return redirect('account:re_activate')
        return f(request, *args, **kwargs)

    wrap.__doc__ = f.__doc__
    wrap.__name__=f.__name__
    return wrap

def is_manager(f):
    def wrap(request, *args, **kwargs):
        check_obj = a_models.user_check.objects.get(user = request.user)
        if not check_obj.manager_status:
            logout(request)
            messages.danger(request, "You do not have permission to visit that area.")
            return redirect('account:login')
        return f(request, *args, **kwargs)

    wrap.__doc__ = f.__doc__
    wrap.__name__=f.__name__
    return wrap