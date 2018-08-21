from .models import *
import random

def event_id_generator():
    reg_no = str(random.randint(100000,999999))
    #reg_no = 'YUIP18'+reg_no
    try:
        up_events.objects.get(event_id=reg_no)
        return event_id_generator()
    except up_events.DoesNotExist:
        return reg_no