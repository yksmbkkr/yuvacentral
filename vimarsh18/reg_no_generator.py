from vimarsh18.models import volunteer, participant
import random

def volunteer_reg_no_generator():
    reg_no = str(random.randint(1000,9999))

    try:
        volunteer.objects.get(reg_no=reg_no)
        return volunteer_reg_no_generator()
    except volunteer.DoesNotExist:
        reg_no = 'VIM18'+reg_no+'V'
        return reg_no

def participant_reg_no_generator():
    reg_no = str(random.randint(10000,99999))

    try:
        participant.objects.get(reg_no=reg_no)
        return participant_reg_no_generator()
    except participant.DoesNotExist:
        reg_no = 'VIM18'+reg_no
        return reg_no