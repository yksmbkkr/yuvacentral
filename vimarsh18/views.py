from django.shortcuts import render
from vimarsh18 import forms as v18_forms
from vimarsh18 import reg_no_generator
from account.views import messages
from django.shortcuts import redirect, HttpResponse, Http404
from django.contrib.auth.decorators import login_required
from vimarsh18 import models as v18_models
from vimarsh18 import email_sender
from account.decorators import *
from account import forms as a_forms
from django.shortcuts import HttpResponseRedirect
from manage_dashboard import models as m_models
from django.contrib.auth.models import User
from vimarsh18 import id_generator as idg
from rest_framework.views import APIView
from rest_framework.response import Response as serial_response
from rest_framework import status
from vimarsh18.serializers import session_vimSerializer

#Vimarsh Home

def vimarsh18_home(request):
    s_list = v18_models.speaker.objects.all()
    args = {
        'slist':s_list
        }
    return render(request, "vimarsh18.html",args)

# Create your views here.
@login_required
@is_profile_created
def volunteer_registration(request):
    messages.error(request,"As of now we have received enough registrations for volunteering therefore volunteer registrations are suspended temporarily. If you are interested leave a mail to cantact@yuva.net.in")
    return redirect('account:activities')
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
    messages.error(request,"As of now we have received enough registrations for volunteering therefore volunteer registrations are suspended temporarily. If you are interested leave a mail to cantact@yuva.net.in")
    return redirect('account:activities')
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

@login_required
@is_profile_created
def participant_registration(request):
    if v18_models.participant.objects.filter(user=request.user).count()>0 :
        messages.warning(request, 'You have already registered for VIMARSH18. Your registration number is '+request.user.participant.reg_no+'. This is also emailed to your registered email ID.')
        return redirect('account:activities')
    if request.user.user_check.profession == 'student':
        form = a_forms.student_info_form()
    else:
        form = a_forms.other_info_form()
    form2 = v18_forms.multiple_choice_form()
    if request.method=='POST':
        if request.user.user_check.profession == 'student':
            form = a_forms.student_info_form(request.POST)
        else:
            form = a_forms.other_info_form(request.POST)
        form2 = v18_forms.multiple_choice_form(request.POST)
        if form.is_valid() and form2.is_valid():
            finalform = form.save(commit=False)
            finalform.user = request.user
            finalform.save()
            choices = form2.cleaned_data.get('choice')
            pay_mode = form2.cleaned_data.get('pay_choice')
            reg_no = reg_no_generator.participant_reg_no_generator()
            p_obj = v18_models.participant(user = request.user, reg_no = reg_no, choice = choices, pay_mode = pay_mode)
            p_obj.save()
            email_sender.participant_email(user=request.user)
            idg.participant_student_id(reg_no)
            if pay_mode == 'pay_online':
                return HttpResponseRedirect('https://www.payumoney.com/paybypayumoney/#/3627569A7B7F8520CC840B9947D94BCA')
            messages.success(request,'Vimarsh 2018 registration successful check your inbox-spambox for further instructions, registration id.')
            if pay_mode == 'pay_college':
                return redirect('vimarsh18:pay_reciept')
            if pay_mode == 'pay_venue':
                return redirect('account:activities')
            return redirect('account:activities')
    return render(request,'participant.html',{'form':form, 'form2':form2})

@login_required
def participant_registration_false(request):
    if v18_models.participant.objects.filter(user=request.user).count()>0 :
        messages.warning(request, 'You have already registered for VIMARSH18. Your registration number is '+request.user.participant.reg_no+'. This is also emailed to your registered email ID.')
        return redirect('account:activities')
    if a_models.profile.objects.filter(user=request.user).count()>0:
        return redirect('vimarsh18:participant_reg')
    if request.user.user_check.profession == 'student':
        form = a_forms.student_info_form()
    else:
        form = a_forms.other_info_form()
    form2 = v18_forms.multiple_choice_form()
    profile_form = a_forms.profile_form()
    if request.method=='POST':
        if request.user.user_check.profession == 'student':
            form = a_forms.student_info_form(request.POST)
        else:
            form = a_forms.other_info_form(request.POST)
        form2 = v18_forms.multiple_choice_form(request.POST)
        profile_form = a_forms.profile_form(request.POST)
        if form.is_valid() and form2.is_valid() and profile_form.is_valid():
            profile_final = profile_form.save(commit=False)
            profile_final.user = request.user
            profile_final.save()
            a_models.user_check.objects.filter(user=request.user).update(profile_status=True)
            messages.success(request,"Profile saved successfully")
            finalform = form.save(commit=False)
            finalform.user = request.user
            finalform.save()
            choices = form2.cleaned_data.get('choice')
            pay_mode = form2.cleaned_data.get('pay_choice')
            reg_no = reg_no_generator.participant_reg_no_generator()
            p_obj = v18_models.participant(user = request.user, reg_no = reg_no, choice = choices, pay_mode = pay_mode)
            p_obj.save()
            email_sender.participant_email(user=request.user)
            idg.participant_student_id(reg_no)
            if pay_mode == 'pay_online':
                return HttpResponseRedirect('https://www.payumoney.com/paybypayumoney/#/3627569A7B7F8520CC840B9947D94BCA')
            messages.success(request,'Vimarsh 2018 registration successful check your inbox-spambox for further instructions, registration id.')
            if pay_mode == 'pay_college':
                return redirect('vimarsh18:pay_reciept')
            if pay_mode == 'pay_venue':
                return redirect('account:activities')
            return redirect('account:activities')
    return render(request,'participant_false.html',{'form':form, 'form2':form2, 'form3':profile_form})

@login_required
def pay_reciept(request):
    if v18_models.participant.objects.filter(user = request.user).count() <1:
        messages.error(request, "You have not yet registered for vimarsh. Please register first")
        return redirect('account:activities')
    if request.user.participant.payment_status:
        messages.info(request, "We have already recieved your payment. ")
        return redirect('account:activities')
    if not request.user.participant.pay_mode == 'pay_college':
        messages.warning(request, "Before proceeding change your payment method. ")
        return redirect('account:activities')
    form = v18_forms.single_field_form()
    if request.method == 'POST':
        form = v18_forms.single_field_form(request.POST)
        if form.is_valid():
            num = form.cleaned_data.get('field1')
            if m_models.vimarsh18_reciept.objects.filter(number = num).count() > 1 :
                messages.error(request, "Invalid reciept. Contact yuva team of your college or contact@yuva.net.in")
                return redirect('vimarsh18:pay_reciept')
            if m_models.vimarsh18_reciept.objects.filter(number = num).count() < 1 :
                messages.error(request, "This reciept has not yet been generated. Ask yuva co-ordinator of your college to generate reciept or mail us at contact@yuva.net.in")
                return redirect('vimarsh18:pay_reciept')
            reciept_obj = m_models.vimarsh18_reciept.objects.get(number = num)
            if reciept_obj.status:
                messages.error(request, "This reciept is already redeemed. Report this issue at contact@yuva.net.in immedietly.")
                return redirect('vimarsh18:pay_reciept')
            m_models.vimarsh18_reciept.objects.filter(number = num).update(used_by = request.user, status = True)
            v18_models.participant.objects.filter(user = request.user).update(payment_status = True)
            subject = 'VIMARSH - Payment Confirmed'
            message = render_to_string('emails/payment_confirmed_email.html',{
                    'user':request.user,
                    'number':num,
                    })
            request.user.email_user(subject,message)
            messages.success(request, "Your payment is confirmed.")
            return redirect('account:activities')
    return render(request, 'pay_reciept.html')

@login_required
@is_profile_created
def change_payment_mode(request):
    if v18_models.participant.objects.filter(user = request.user).count() <1:
        messages.error(request, "You have not yet registered for vimarsh. Please register first")
        return redirect('account:activities')
    if request.user.participant.payment_status:
        messages.info(request, "We have already recieved your payment. ")
        return redirect('account:activities')
    form = v18_forms.single_choice_form()
    current_method = request.user.participant.pay_mode
    if current_method == 'pay_online':
        current_method = "Pay Online"
    elif current_method == 'pay_college':
        current_method = "Pay/Paid at College"
    else:
        current_method = "Will pay at venue during Vimarsh"
    if request.method == 'POST':
        form = v18_forms.single_choice_form(request.POST)
        if form.is_valid():
            current_method = request.user.participant.pay_mode
            if current_method == 'pay_online':
                current_method = "Pay Online"
            elif current_method == 'pay_college':
                current_method = "Pay/Paid at College"
            else:
                current_method = "Will pay at venue during Vimarsh"
            new_method = form.cleaned_data.get('pay_choice')
            v18_models.participant.objects.filter(user = request.user).update(pay_mode = new_method)
            messages.success(request, "Payment Method changed successfully.")
            return redirect('account:activities')
    return render(request, 'change_payment.html', {'form':form, 'cp' : current_method})

@login_required
@is_manager
def idtry(request,user_id = None):
    image = idg.participant_student_id(user_id)
    #response = HttpResponse(content_type="image/png")
    #image.save(response, "PNG")
    return HttpResponse('Success')

@login_required
@is_manager
def all_participant_idcard(request):
    list1 = v18_models.participant.objects.all()
    for l in list1:
        num = l.reg_no
        if v18_models.id_card.objects.filter(reg_no = num).count() < 1:
            idg.participant_student_id(num)
    return HttpResponse(v18_models.id_card.objects.all().count())

@login_required
@is_manager
def all_volunteer_idcard(request):
    list1 = v18_models.volunteer.objects.all()
    for l in list1:
        num = l.reg_no
        if v18_models.id_card.objects.filter(reg_no = num).count() < 1:
            idg.participant_student_id(num)
    return HttpResponse(v18_models.id_card.objects.all().count())

def mark_attendance(request, rid = None, sid = None):
    if rid==None or sid==None:
        raise Http404
    try:
        p_obj = v18_models.participant.objects.get(reg_no = rid)
        user = p_obj.user
    except v18_models.participant.DoesNotExist:
        #print("p not exist")
        raise Http404
    try:
        s_obj = v18_models.session_vim.objects.get(sid = sid)
    except v18_models.session_vim.DoesNotExist:
        #print("s not exist")
        raise Http404
    if v18_models.attendance.objects.filter(rid = rid, sid = sid).count() > 0:
        #print('already here')
        return HttpResponse(status = 200)
    a_obj = v18_models.attendance(rid = rid, sid = s_obj, user = user)
    a_obj.save()
    return HttpResponse(status=200)



def payment_successful(request):
    return render(request, 'payment_successful.html')

def payment_failed(request):
    return render(request, 'payment_failed.html')

def payment_pending(request):
    return render(request, 'payment_pending.html')

class session_vimList(APIView):
    def get(self,request):
        sessions = v18_models.session_vim.objects.all()
        serializer = session_vimSerializer(sessions, many = True)
        return serial_response(serializer.data)

    def post(self):
        pass