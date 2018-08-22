from django.shortcuts import render, redirect, Http404
from django.contrib.auth.decorators import login_required
from manage_dashboard import forms as m_forms
from manage_dashboard.custom_generators import *
from account.decorators import *

# Create your views here.

def template_test(request):
    return render(request, 'manage/upcoming-events.html',{'form':m_forms.upcoming_events_form()})

@login_required
@is_profile_created
@is_manager
def add_upcoming_events(request):
    if request.user.is_authenticated()==False:
        return redirect('landing:login')
    if request.user.is_staff==False:
        raise Http404
    form = m_forms.upcoming_events_form()
    if request.method=='POST':
        form = m_forms.upcoming_events_form(request.POST, request.FILES)
        if form.is_valid():
            finalform=form.save(commit=False)
            eid = event_id_generator()
            finalform.event_id = eid
            finalform.save()
            return redirect('landing:home')
    return render(request,'manage/upcoming-events.html',{'form':form})
