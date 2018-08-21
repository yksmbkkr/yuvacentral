from django.shortcuts import render, redirect, Http404
from manage_dashboard import forms as m_forms
from manage_dashboard.custom_generators import *
# Create your views here.

def template_test(request):
    return render(request, 'manage/upcoming-events.html',{'form':m_forms.upcoming_events_form()})

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
