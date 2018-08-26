from django.shortcuts import render
from manage_dashboard import models as m_models

# Create your views here.

def home(request):
    upcoming_event_list = m_models.up_events.objects.filter(to_post = True)
    elist=False
    if upcoming_event_list.count()>0:
        elist=True
    return render(request, 'yuva.html',{'up_eve':upcoming_event_list,'elist':elist})
