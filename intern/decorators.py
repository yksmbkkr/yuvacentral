from intern.models import *
from django.shortcuts import redirect


def is_intern_data_created(f):
    def wrap(request, *args, **kwargs):
        profile_object = intern_data.objects.filter(user = request.user).count()
        if profile_object<1:
            return redirect('intern:create_profile')
        return f(request, *args, **kwargs)

    wrap.__doc__ = f.__doc__
    wrap.__name__=f.__name__
    return wrap

