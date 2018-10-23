from django.shortcuts import render, redirect, Http404
from django.shortcuts import HttpResponse
from django.contrib.sites.shortcuts import get_current_site
from django.template.loader import render_to_string
from django.core.mail import send_mail, get_connection
from django.contrib.auth.decorators import login_required
from random import *
import string
from manage_dashboard import forms as m_forms
from manage_dashboard.custom_generators import *
from account.decorators import *
from manage_dashboard import models as m_models
from django.contrib.auth.models import User
from account import forms as a_forms
from vimarsh18 import models as v18_models
from slugify import slugify
from PIL import Image, ImageDraw, ImageFont
from io import BytesIO
from vimarsh18.id_generator import text_wrap
from django.core.files.base import ContentFile
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
    participants = v18_models.participant.objects.all().count()
    participants_paid = v18_models.participant.objects.filter(payment_status = True).count()
    participants_pay_online = v18_models.participant.objects.filter(pay_mode = 'pay_online').count()
    participants_pay_college = v18_models.participant.objects.filter(pay_mode = 'pay_college').count()
    participants_pay_venue = v18_models.participant.objects.filter(pay_mode = 'pay_venue').count()
    participants_pay_online_paid = v18_models.participant.objects.filter(pay_mode = 'pay_online', payment_status = True).count()
    participants_pay_college_paid = v18_models.participant.objects.filter(pay_mode = 'pay_college', payment_status = True).count()
    participants_pay_venue_paid = v18_models.participant.objects.filter(pay_mode = 'pay_venue', payment_status = True).count()
    reciepts_generated = m_models.vimarsh18_reciept.objects.all().count()
    reciepts_used = m_models.vimarsh18_reciept.objects.filter(status = True).count()
    arg = {
        'lc':live_count,
        'oc':offline_count,
        'tc':total_count,
        'dh':'active',
        'uc':user_count,
        'uec':user_with_email_confirmed,
        'upc':user_profile_completed,
        'umc':user_managers,
        'participants':participants,
        'participants_paid':participants_paid,
        'participants_pay_online':participants_pay_online,
        'participants_pay_college':participants_pay_college,
        'participants_pay_venue':participants_pay_venue,
        'participants_pay_online_paid':participants_pay_online_paid,
        'participants_pay_college_paid':participants_pay_college_paid,
        'participants_pay_venue_paid':participants_pay_venue_paid,
        'reciepts_generated':reciepts_generated,
        'reciepts_used':reciepts_used
        }
    return render(request,'manage/dashboard.html',arg)

@login_required
@is_profile_created
@is_manager
def add_manager(request):
    form = a_forms.single_field_form()
    if request.method=='POST':
        form = a_forms.single_field_form(request.POST)
        if form.is_valid():
            email = form.cleaned_data['field1']
            if User.objects.filter(username = email).count()<1:
                username = email
            else:
                messages.error(request,"Unable to verify. Use defferent email address")
                return redirect('dashboard:add_manager')
            try:
                usr = User.objects.get(email=email)
                usr.manager_status = True
                usr.save()
                subject = 'YUVA Account - Admin level privileges granted'
                message = render_to_string('manage/existing_add_manager_email.html',{
                    'user':usr,
                    })
                usr.email_user(subject,message)
                messages.success(request, "Admin privileges granted to the user")
            except User.DoesNotExist:
                min_char = 12
                max_char = 20
                allchar = string.ascii_letters + string.punctuation + string.digits
                passwd = "".join(choice(allchar) for x in range(randint(min_char, max_char)))
                usr = User.objects.create_user(username = username, email = email, password=passwd)
                user_check_obj = a_models.user_check(user=usr, manager_status=True, email_confirmation_status=True)
                user_check_obj.save()
                subject = 'YUVA Account - Account created | Admin level privileges granted'
                message = render_to_string('manage/new_add_manager_email.html',{
                    'user':usr,
                    })
                usr.email_user(subject,message)
                messages.success(request, "Account with admin level privileges created and mail is sent.")
    return render(request,'manage/add_manager.html', {'am':'active'})

@login_required
@is_profile_created
@is_manager
def add_reciept_manager(request):
    form = a_forms.single_field_form()
    if request.method=='POST':
        form = a_forms.single_field_form(request.POST)
        if form.is_valid():
            email = form.cleaned_data['field1']
            if User.objects.filter(email = email).count()<1:
                messages.error(request,"No such user is registered.")
                return redirect('dashboard:add_reciept_manager')
            usr = User.objects.get(email = email)
            a_models.user_check.objects.filter(user = usr).update(reciept_manager_status = True)
            subject = 'YUVA Account - Reciept generation privileges granted'
            message = render_to_string('manage/add_reciept_manager_email.html',{
                    'user':usr,
                    })
            usr.email_user(subject,message)
            messages.success(request, "Reciept generation privileges granted to the user")
            return redirect('dashboard:add_reciept_manager')
    return render(request, 'manage/add_reciept_manager.html', {'arm': 'active'})

@login_required
@is_profile_created
def generate_reciept(request):
    if not request.user.user_check.reciept_manager_status == True:
        messages.error(request,"You don't have permission to generate reciepts. Contact admin at admin@yuva.net.in ")
        return redirect('account:activities')
    form = a_forms.single_field_form()
    if request.method=='POST':
        form = a_forms.single_field_form(request.POST)
        if form.is_valid():
            creator = request.user
            reciept_number = form.cleaned_data.get('field1')
            if m_models.vimarsh18_reciept.objects.filter(number = reciept_number).count() >0:
                reciept = m_models.vimarsh18_reciept.objects.get(number = reciept_number)
                messages.error(request, "Reciept with number "+reciept_number+" already exists. It is created by "+
                               reciept.creator.username+". You can contact him or her at "+reciept.creator.email)
                return redirect('dashboard:generate_reciept')
            reciept_obj = m_models.vimarsh18_reciept(number = reciept_number, creator = creator)
            reciept_obj.save()
            messages.success(request, "Reciept with number "+reciept_number+" is created successfully by "+creator.username)
            return redirect('dashboard:generate_reciept')
    return render(request, 'manage/generate_reciept.html',{'gr':'active'})

@login_required
@is_profile_created
@is_manager
def online_payment_confirmation(request):
    form = a_forms.single_field_form()
    if request.method=='POST':
        form = a_forms.single_field_form(request.POST)
        if form.is_valid():
            reg_no = form.cleaned_data.get('field1')
            if v18_models.participant.objects.filter(reg_no = reg_no).count() < 1:
                messages.error(request, "No participant with registration number "+reg_no+" exists.")
                return redirect('dashboard:online_payment_confirmation')
            v18_models.participant.objects.filter(reg_no = reg_no).update(payment_status = True)
            messages.success(request, "Payment of participant with registration number "+reg_no+" is confirmed.")
            usr = v18_models.participant.objects.get(reg_no = reg_no).user
            subject = 'VIMARSH 2018 - Payment Confirmation'
            message = render_to_string('manage/online_payment_confirmation_email.html',{
                    'user':usr,
                    })
            usr.email_user(subject,message)
            return redirect('dashboard:online_payment_confirmation')
    return render(request, 'manage/online_payment_confirmation.html', {'opc':'active'})

@login_required
@is_profile_created
@is_manager
def volunteer_list(request):
    v_list = v18_models.volunteer.objects.all()
    return render(request,'manage/vv_list.html',{'vvl':'active', 'vlist':v_list})

@login_required
@is_profile_created
@is_manager
def participant_list(request):
    p_list = v18_models.participant.objects.all()
    return render(request, 'manage/plist.html',{'plist':p_list, 'pl':'active'})

@login_required
@is_profile_created
@is_manager
def reciept_list(request):
    r_list = m_models.vimarsh18_reciept.objects.all()
    return render(request, 'manage/rlist.html',{'rlist':r_list, 'rl':'active'})

def reciept_manager_list(request):
    rm_llist = a_models.profile.objects.filter(user__user_check__reciept_manager_status = True)
    rm_list = []
    for r in rm_llist:
        c = r.user.reciept_manager.all().filter(status=True).count()
        temp = {
            'r':r,
            'c':c
            }
        rm_list.append(temp)
    return render(request, 'manage/rmlist.html',{'rmlist':rm_list, 'rml':'active'})

@login_required
@is_profile_created
@is_manager
def speaker(request, id = None):
    s_list = v18_models.speaker.objects.all()
    if id==None:
        form = m_forms.speaker_form()
        if request.method == 'POST':
            form = m_forms.speaker_form(request.POST, request.FILES)
            if form.is_valid():
                form.save()
                messages.success(request, "Speaker added successfully")
                return redirect('dashboard:speaker')
        return render(request, 'manage/speaker.html', {'form':form, 'spk':'active', 'slist':s_list})
    else:
        try:
            speaker_obj = v18_models.speaker.objects.get(id = id)
        except v18_models.speaker.DoesNotExist:
            messages.error(request, "No such speaker exists")
            return redirect('dashboard:speaker')
        form = m_forms.speaker_form(instance = speaker_obj)
        if request.method == 'POST':
            form = m_forms.speaker_form(request.POST, request.FILES,  instance = speaker_obj)
            if form.is_valid():
                form.save()
                messages.success(request, "Speaker updated successfully")
                return redirect('dashboard:speaker')
        return render(request, 'manage/speaker.html', {'form':form, 'spk':'active', 'slist':s_list})

@login_required
@is_profile_created
@is_manager
def session_vim(request, id =None):
    s_list = v18_models.session_vim.objects.all()
    if id == None:
        form = m_forms.session_vim_form()
        if request.method=='POST':
            form = m_forms.session_vim_form(request.POST)
            if form.is_valid():
                sid = session_vim_id_generator()
                finalform = form.save(commit = False)
                finalform.sid = sid
                finalform.save()
                messages.success(request, "Session created successfully")
                return redirect('dashboard:session_vim')
        return render(request, 'manage/session_vim.html', {'form':form, 'snvm':'active','slist':s_list})
    else:
        try:
            session_vim_obj = v18_models.session_vim.objects.get(sid = str(id))
        except v18_models.session_vim.DoesNotExist:
            messages.error(request,"Session does not exist.")
            return redirect('dashboard:session_vim')
        form = m_forms.session_vim_form(instance = session_vim_obj)
        if request.method == 'POST':
            form = m_forms.session_vim_form(request.POST, instance = session_vim_obj)
            if form.is_valid():
                form.save()
                messages.success(request, "Session updated successfuly")
                return redirect('dashboard:session_vim')
        return render(request, 'manage/session_vim.html', {'form':form, 'snvm':'active', 'slist':s_list})

@login_required
@is_profile_created
@is_manager
def get_non_participant_list(request):
    list3 = User.objects.filter(participant__isnull = True, volunteer__isnull = True)
    print(list3)
    args = {
        'list1':list3
        }
    return render(request,'manage/non_p_list.html',args)

@login_required
def offline_payment(request):
    if not request.user.user_check.manager_status and not request.user.user_check.venue_payment_permission:
        raise Http404
    form = a_forms.single_field_form()
    if request.method=='POST':
        form = a_forms.single_field_form(request.POST)
        if form.is_valid():
            reg_no = form.cleaned_data.get('field1')
            reg_no = str(reg_no)
            if not 'VIM18' in reg_no:
                reg_no = 'VIM18'+reg_no
            if v18_models.participant.objects.filter(reg_no = reg_no).count() < 1:
                messages.error(request, "No participant with registration number "+reg_no+" exists.")
                return redirect('dashboard:offline_payment')
            if v18_models.venue_payment_stats.objects.filter(payee_id = reg_no).count() > 0:
                p_obj = v18_models.venue_payment_stats.obects.get(payee_id = reg_no)
                messages.error(request, "Payment of participant with registration number "+reg_no+" is already done please report it to admin.")
                return redirect('dashboard:offline_payment')
            p_obj = v18_models.venue_payment_stats(collector = request.user, payee_id = reg_no)
            p_obj.save()
            v18_models.participant.objects.filter(reg_no = reg_no).update(payment_status = True)
            messages.success(request, "Payment of participant with registration number "+reg_no+" is confirmed.")
            usr = v18_models.participant.objects.get(reg_no = reg_no).user
            subject = 'VIMARSH 2018 - Payment Confirmation'
            message = render_to_string('manage/online_payment_confirmation_email.html',{
                    'user':usr,
                    })
            usr.email_user(subject,message)
            return redirect('dashboard:offline_payment')
    return render(request, 'manage/offline_payment.html', {'form':form, 'ofc':'active'})

@login_required
@is_manager
def id_creator(request):
    form = m_forms.id_choice_form()
    if request.method == 'POST':
        form = m_forms.id_choice_form(request.POST)
        if form.is_valid():
            name = form.cleaned_data['name']
            id_type = form.cleaned_data['id_type']
            filename = slugify(name)+'.png'
            if id_type == 'guest':
                bg_url = '/home/adminyash/yuvacentral/vimarsh18/static/icard/guest.png'
                #bg_url = 'C:/Users/Yash Kulshreshtha/source/repos/yuvacentral/yuvacentral/vimarsh18/static/icard/guest.png'
            elif id_type == 'organiser':
                bg_url = '/home/adminyash/yuvacentral/vimarsh18/static/icard/organiser.png'
                #bg_url = 'C:/Users/Yash Kulshreshtha/source/repos/yuvacentral/yuvacentral/vimarsh18/static/icard/organiser.png'
            else:
                bg_url = '/home/adminyash/yuvacentral/vimarsh18/static/icard/vsn.png'
                #bg_url = 'C:/Users/Yash Kulshreshtha/source/repos/yuvacentral/yuvacentral/vimarsh18/static/icard/vsn.png'
            bg = Image.open(bg_url)
            img_io = BytesIO()
            draw =  ImageDraw.Draw(bg)
            font = ImageFont.truetype(font='/home/adminyash/yuvacentral/vimarsh18/static/icard/calibri.ttf',size = 22)
            #font = ImageFont.truetype(font='C:/Users/Yash Kulshreshtha/source/repos/yuvacentral/yuvacentral/vimarsh18/static/icard/calibri.ttf',size = 22)
            text_data = text_wrap(name[:40],font,310)
            draw.text((60,310),text_data,fill = (1,72,174), font = font)
            bg.save(img_io, bg.format, quality=50)
            id_obj = v18_models.id_special(name = name)
            id_obj.id_img.save(filename, ContentFile(img_io.getvalue()), save=False)
            id_obj.save()
            response = HttpResponse(content_type="image/png")
            image = bg
            image.save(response, "PNG")
            return response
    return render(request,'manage/id_special.html',{'form':form,'id_creator':'active'})