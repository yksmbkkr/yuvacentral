from vimarsh18.models import volunteer
import random

def volunteer_reg_no_generator():
    reg_no = str(random.randint(1000,9999))

    try:
        volunteer.objects.get(reg_no=reg_no)
        return volunteer_reg_no_generator()
    except volunteer.DoesNotExist:
        reg_no = 'VIM18'+reg_no+'V'
        return reg_no