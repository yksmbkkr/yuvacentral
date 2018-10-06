from .models import *
import random
from vimarsh18 import models as v18_models

def event_id_generator():
    reg_no = str(random.randint(100000,999999))
    #reg_no = 'YUIP18'+reg_no
    try:
        up_events.objects.get(event_id=reg_no)
        return event_id_generator()
    except up_events.DoesNotExist:
        return reg_no

def session_vim_id_generator():
    sid = str(random.randint(1000,9999))
    try:
        v18_models.session_vim.objects.get(sid = sid)
        return session_vim_id_generator()
    except v18_models.session_vim.DoesNotExist:
        return sid