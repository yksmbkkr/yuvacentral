from django.shortcuts import render, redirect
from manage_dashboard import models as m_models

# Create your views here.

def home(request):
    upcoming_event_list = m_models.up_events.objects.filter(to_post = True)
    elist=False
    if upcoming_event_list.count()>0:
        elist=True
    return render(request, 'yuva.html',{'up_eve':upcoming_event_list,'elist':elist})

def login_redirect(request):
    next_route = request.GET.get('next')
    if not next_route:
        return redirect('landing:login')
    return redirect('/login/login/?next='+next_route)