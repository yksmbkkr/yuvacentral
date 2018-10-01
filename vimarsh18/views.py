from django.shortcuts import render
from vimarsh18 import forms as v18_forms
from vimarsh18 import reg_no_generator
from account.views import messages
from django.shortcuts import redirect
from django.contrib.auth.decorators import login_required
from vimarsh18 import models as v18_models
from vimarsh18 import email_sender
from account.decorators import *
from account import forms as a_forms

# Create your views here.
@login_required
@is_profile_created
def volunteer_registration(request):
    if v18_models.volunteer.objects.filter(user=request.user).count()>0 :
        messages.warning(request, 'You have already registered as voluteer. Your volunteer registration number is '+request.user.volunteer.reg_no+'. This is also emailed to your registered email ID.')
        return redirect('account:activities')
    form=v18_forms.volunteer_form()
    if request.method=='POST':
        form = v18_forms.volunteer_form(request.POST)
        if form.is_valid:
            finalform = form.save(commit=False)
            finalform.user = request.user
            reg_no = reg_no_generator.volunteer_reg_no_generator()
            finalform.reg_no = reg_no
            
            email_sender.volunteer_email(user=request.user)
            messages.success(request,'Your volunteering application accepted successfully check your inbox-spambox for further instructions.')
            finalform.save()
            return redirect('account:activities')
    return render(request,'volunteer.html',{'form':form})

@login_required
def volunteer_registration_false(request):
    if v18_models.volunteer.objects.filter(user=request.user).count()>0 :
        messages.warning(request, 'You have already registered as voluteer. Your volunteer registration number is '+request.user.volunteer.reg_no+'. This is also emailed to your registered email ID.')
        return redirect('account:activities')
    if a_models.profile.objects.filter(user=request.user).count()>0:
        return redirect('vimarsh18:volunteer_reg')
    profile_form = a_forms.profile_form()
    volunteer_form = v18_forms.volunteer_form()
    if request.method=='POST':
        profile_form = a_forms.profile_form(request.POST)
        volunteer_form = v18_forms.volunteer_form(request.POST)
        if profile_form.is_valid() and volunteer_form.is_valid():
            profile_final = profile_form.save(commit=False)
            volunteer_final = volunteer_form.save(commit=False)
            profile_final.user = request.user
            profile_final.save()
            a_models.user_check.objects.filter(user=request.user).update(profile_status=True)
            messages.success(request,"Profile saved successfully")
            volunteer_final.user = request.user
            reg_no = reg_no_generator.volunteer_reg_no_generator()
            volunteer_final.reg_no = reg_no
            email_sender.volunteer_email(user=request.user)
            messages.success(request,'Your volunteering application accepted successfully check your inbox-spambox for further instructions.')
            volunteer_final.save()
            return redirect('account:activities')
    return render(request,  'volunteer_false.html',{'form1':profile_form, 'form2':volunteer_form})

def payment_successful(request):
    return render(request, 'payment_successful.html')

def payment_failed(request):
    return render(request, 'payment_failed.html')

def payment_pending(request):
    return render(request, 'payment_pending.html')