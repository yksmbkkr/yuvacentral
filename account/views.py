from django.shortcuts import render, redirect
from django.contrib.sites.shortcuts import get_current_site
from django.http import HttpResponse, Http404, HttpResponseRedirect
from django.core.mail import send_mail, get_connection
from django.contrib import messages
import datetime
from django.utils import timezone
from django.core.mail import EmailMultiAlternatives
from django.contrib.auth.forms import PasswordResetForm
from django.template.loader import get_template
from django.template import Context
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout
from django.contrib.admin.views.decorators import staff_member_required
from django.contrib.auth import login, authenticate
from django.contrib.auth.models import User
from django.utils.encoding import force_text, force_bytes
from django.utils.http import urlsafe_base64_decode, urlsafe_base64_encode
from django.template.loader import render_to_string
from django.http import HttpResponse
from wsgiref.util import FileWrapper
import csv, os
from django.conf import settings

from account import forms as a_forms
from account import models as a_models
from account.tokens import email_confirmation_token
from account.decorators import *
from vimarsh18 import models as v18_models

# Create your views here.

#template_test
def template_test(request):
    form = a_forms.profile_form()
    return render(request,'profile.html',{'form':form})

def register_yuva(request):
    v = str(request.GET.get('v','no'))
    if request.user.is_authenticated():
        return redirect('account:profile')
    form = a_forms.registration_form()
    form2 = a_forms.profession_choice_form()
    if request.method=='POST':
        form = a_forms.registration_form(request.POST)
        form2 = a_forms.profession_choice_form(request.POST)
        if form.is_valid() and form2.is_valid():
            prof = form2.cleaned_data.get('profession')
            emailad = form.cleaned_data.get('email')
            if User.objects.filter(email=emailad).count() > 0 :
                messages.error(request, 'User with the submitted email id is already registered.')
                return redirect('account:register_yuva')
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            login(request, user)
            user_check_obj = a_models.user_check(user=request.user, profession = prof)
            user_check_obj.save()
            current_site = get_current_site(request)
            subject = 'YUVA Account - Confirm Your Email Address'
            message = render_to_string('email_confirmation_email.html',{
                    'user':user,
                    'domain':current_site.domain,
                    'uid':urlsafe_base64_encode(force_bytes(user.pk)),
                    'token':email_confirmation_token.make_token(user),
                    })
            user.email_user(subject,message)
            messages.info(request, 'Account created successfully. Check your inbox and spambox and confirm your account.')
            if v=='vl':
                return redirect('vimarsh18:volunteer_reg_false')
            if v=='v':
                return redirect('vimarsh18:participant_reg_false')
            return redirect('account:profile')
    return render(request,'register.html',{'form':form, 'form2':form2})

def activation(request, uidb64, token):
    try:
        uid = force_text(urlsafe_base64_decode(uidb64))
        user = User.objects.get(pk = uid)
    except (TypeError, ValueError, OverflowError, User.DoesNotExist):
        user = None

    if user is not None and email_confirmation_token.check_token(user, token):
        user.user_check.email_confirmation_status = True
        user.save()
        a_models.user_check.objects.filter(user=user).update(email_confirmation_status = True)
        messages.success(request,"Your Email ID is confirmed successfully")
        return redirect('account:profile')
    else:
        messages.danger(request,"Either this activation link is invalid or expired ! Try Again...")
        return redirect('account:re_activate')

@login_required
@is_confirm_mail
def profile(request):
    if a_models.profile.objects.filter(user=request.user).count()>0:
        form=a_forms.profile_form(instance = a_models.profile.objects.get(user = request.user))
        if request.method=='POST':
            form = a_forms.profile_form(request.POST,instance = a_models.profile.objects.get(user = request.user))
            if form.is_valid():
                form.save()
                messages.success(request,"Changes in your profile saved successfully")
                return redirect('account:profile')
        return render(request,'profile.html',{'form':form, 'profile_pill':'active'})
    form = a_forms.profile_form()
    if request.method=='POST':
        form = a_forms.profile_form(request.POST)
        if form.is_valid():
            finalform = form.save(commit=False)
            finalform.user = request.user
            finalform.save()
            a_models.user_check.objects.filter(user=request.user).update(profile_status=True)
            messages.success(request,"Profile saved successfully")
            return redirect('account:profile')
    return render(request,'profile.html',{'form':form, 'profile_pill':'active'})

@login_required
def activation_status(request):
    if request.user.user_check.email_confirmation_status:
        return redirect('/')
    return render(request,'resend-confirmation.html')

@login_required
def create_reactivation(request):
    user = request.user
    a_models.user_check.objects.filter(user=request.user).update(email_confirmation_status=False)
    current_site = get_current_site(request)
    subject = 'YUVA Account - Confirm Your Email Address'
    message = render_to_string('email_confirmation_email.html',{
                    'user':user,
                    'domain':current_site.domain,
                    'uid':urlsafe_base64_encode(force_bytes(user.pk)),
                    'token':email_confirmation_token.make_token(user),
                    })
    user.email_user(subject,message)
    logout(request)
    messages.warning(request,"Successfully resent confirmation mail. You need to creconfirm your account. Check your inbox and spambox.")
    return redirect('landing:login')

def forgot_password(request):
    if request.user.is_authenticated():
        messages.warning(request,"You are already logged in. Logout and try.")
        return redirect('account:profile')
    form = a_forms.single_field_form()
    if request.method=='POST':
        form = a_forms.single_field_form(request.POST)
        if form.is_valid():
            emailad = form.cleaned_data['field1']
            if User.objects.filter(email=emailad).count()==0:
                messages.error(request, "Email ID "+emailad+" is not registerd with us.")
                return redirect('account:forgot_password')
            pass_form = PasswordResetForm({'email':emailad})
            if pass_form.is_valid():
                print("working")
                pass_form.save(request=request, subject_template_name = 'password_reset_subject.txt', email_template_name='password_reset_email.html', from_email="no-reply@yuva.net.in", )
                messages.success(request, 'Password reset email is sent to the provided address. Check inbox and spambox.')
                return redirect('account:forgot_password')
    return render(request,'forgot-password.html')

@login_required
def change_mail(request):
    form = a_forms.single_field_form()
    if request.method=='POST':
        form = a_forms.single_field_form(request.POST)
        if form.is_valid():
            usr = request.user
            email = form.cleaned_data['field1']
            if User.objects.filter(email = email).count()>0:
                messages.error(request, email+" is already associated with another account. Use forget password option to recover password.")
                return redirect('landing:login')
            usr.email = email
            usr.save()
            messages.success(request,"Your email address is updated successfully.")
            return redirect('account:create_reactivation')
    return render(request, "email-update.html",{'form':form})

@login_required
@is_profile_created
def activities(request):
    volunteering_list = v18_models.volunteer.objects.filter(user=request.user)
    p_list = v18_models.participant.objects.filter(user=request.user)
    return render(request, 'activities.html',{'activities_pill':'active','vol_list':volunteering_list, 'plist':p_list})
