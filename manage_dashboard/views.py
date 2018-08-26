from django.shortcuts import render, redirect, Http404
from django.contrib.auth.decorators import login_required
from manage_dashboard import forms as m_forms
from manage_dashboard.custom_generators import *
from account.decorators import *
from manage_dashboard import models as m_models
from django.contrib.auth.models import User
from account import models as a_models

# Create your views here.

def template_test(request):
    return render(request, 'manage/upcoming-events.html',{'form':m_forms.upcoming_events_form()})

@login_required
@is_profile_created
@is_manager
def add_upcoming_events(request, id = None):
    if request.user.is_authenticated()==False:
        return redirect('landing:login')
    if id != None:
        id = int(id)
        try:
            event_obj = m_models.up_events.objects.get(event_id = id)
        except m_models.up_events.DoesNotExist:
            messages.error(request,"No such event exists")
            return redirect('dashboard:list_upcoming_events')
        form = m_forms.upcoming_events_form(instance = event_obj)
        if request.method=='POST':
            form = m_forms.upcoming_events_form(request.POST, request.FILES, instance = event_obj)
            if form.is_valid():
                form.save()
                messages.success(request,"Changes in event saved successfuly.")
                return redirect('dashboard:list_upcoming_events')
        return render(request,'manage/upcoming-events.html',{'form':form,'u_eve':'active'})
    form = m_forms.upcoming_events_form()
    if request.method=='POST':
        form = m_forms.upcoming_events_form(request.POST, request.FILES)
        if form.is_valid():
            finalform=form.save(commit=False)
            eid = event_id_generator()
            finalform.event_id = eid
            finalform.save()
            return redirect('dashboard:list_upcoming_events')
    return render(request,'manage/upcoming-events.html',{'form':form,'u_eve':'active'})

@login_required
@is_profile_created
@is_manager
def upcoming_events_list(request):
    up_eve_posted = m_models.up_events.objects.filter(to_post = True)
    up_eve_not_posted = m_models.up_events.objects.filter(to_post = False)
    return render(request, 'manage/up-events-list.html', {'u_eve':'active','up_eve':up_eve_posted,'up_eve_not':up_eve_not_posted})

@login_required
@is_profile_created
@is_manager
def make_event_live(request, id = None, status = None):
    status = int(status)
    id = int(id)
    try:
        event_obj = m_models.up_events.objects.get(event_id=id)
    except m_models.up_events.DoesNotExist:
        messages.error(request,"No such event exists")
        return redirect('dashboard:list_upcoming_events')
    if status == 1:
        event_obj.to_post = True
        event_obj.save()
        #event_obj.update(to_post = True)
        messages.success(request,"Event "+event_obj.name+" is live now.")
    else:
        event_obj.to_post = False
        event_obj.save()
        #event_obj.update(to_post = False)
        messages.warning(request,"Event "+event_obj.name+" is offline now.")
    return redirect('dashboard:list_upcoming_events')

@login_required
@is_profile_created
@is_manager
def dash_home(request):
    live_count = m_models.up_events.objects.filter(to_post = True).count()
    offline_count = m_models.up_events.objects.filter(to_post = False).count()
    total_count = live_count+offline_count
    user_count = User.objects.all().count()
    user_with_email_confirmed = a_models.user_check.objects.filter(email_confirmation_status = True).count()
    user_profile_completed = a_models.user_check.objects.filter(profile_status = True).count()
    user_managers = a_models.user_check.objects.filter(manager_status = True).count()
    arg = {
        'lc':live_count,
        'oc':offline_count,
        'tc':total_count,
        'dh':'active',
        'uc':user_count,
        'uec':user_with_email_confirmed,
        'upc':user_profile_completed,
        'umc':user_managers
        }
    return render(request,'manage/dashboard.html',arg)
