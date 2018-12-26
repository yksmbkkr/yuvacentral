from intern.models import intern_registration
import random

def reg_no_generator():
    reg_no = str(random.randint(1000,9999))
    reg_no = 'YUIP18'+reg_no

    try:
        intern_registration.objects.get(reg_no=reg_no)
        return reg_no_generator()
    except intern_registration.DoesNotExist:
        return reg_no