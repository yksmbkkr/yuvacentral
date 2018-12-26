from django.shortcuts import render, redirect
from django.contrib.sites.shortcuts import get_current_site
from intern.reg_no_generator import reg_no_generator
from intern.pdfGenerator import generate_pdf
from django.http import HttpResponse, Http404, HttpResponseRedirect
from django.core.mail import send_mail, get_connection
from django.contrib import messages
from intern.forms import *
from intern.models import *
import datetime
from django.utils import timezone
from django.core.mail import EmailMultiAlternatives
from django.template.loader import get_template
from django.template import Context
from django.contrib.auth.decorators import login_required
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
from django.contrib.auth.decorators import login_required
from account.decorators import *
from intern.decorators import *
from account import models as a_models


def intern_home(request):
    return render(request,'intern/intern_home.html')

def intern_field(request):
    return render(request, 'intern/field_intern.html')

@login_required
def create_profile(request):
    if request.method == 'POST':
        form = intern_data_form(request.POST, request.FILES)
        if form.is_valid():
            finalform=form.save(commit=False)
            finalform.user = request.user
            finalform.save()
            return redirect('account:activities')
    else:
        form = intern_data_form()
    return render(request,'intern/create_profile.html',{'form':form})

@login_required
@is_profile_created
def pdf_download(request):
    p = profile.objects.get(user= request.user)
    file = p.resume
    response = HttpResponse(FileWrapper(file), content_type='application/pdf')
    response['Content-Disposition'] = 'attachment; filename=resume.pdf'
    return response

@login_required
@is_profile_created
@is_intern_data_created
def apply_intern(request, intern_choice):
    try:
        intern_choice = str(intern_choice)
    except ValueError:
        raise Http404
    intern_object = intern_code.objects.get(code = intern_choice)
    try:
        if intern_registration.objects.filter(user = request.user, code = intern_choice).count()>0:
            messages.error(request, 'You have already applied for '+intern_object.intern)
            return redirect('account:activities')
    except intern_registration.DoesNotExist:
        pass
    
    regno = reg_no_generator()
    intern_registration_object = intern_registration(user = request.user, code = intern_object, reg_no=regno)

    plaintext = get_template('intern/email.txt')
    htmly = get_template('intern/email.html')

    profile_obj = a_models.profile.objects.get(user=request.user)
    con = get_connection('django.core.mail.backends.smtp.EmailBackend')     
    d = {'name':profile_obj.name, 'intern':intern_object.intern, 'field':intern_object.field, 'regno':regno}
    subject, from_email, to = 'Regards from Team YUVA', 'YUVA<contact@yuva.net.in>',request.user.email
    text_content = plaintext.render(d)
    html_content = htmly.render(d)
    msg = EmailMultiAlternatives(subject, text_content, from_email, [to])
    msg.attach_alternative(html_content, "text/html")
    msg.send()

    intern_registration_object.save()
    
    messages.success(request, 'You have successfully applied for '+intern_object.intern+' internship in '+intern_object.field+' field.')
    return redirect('account:activities')

@login_required
@is_manager
def view_reg(request):
    user_set = User.objects.all()
    total_list = []
    for u in user_set :
        try:
            p = a_models.profile.objects.get(user = u)
            a_data = intern_data.objects.get(user = u)
            i = intern_registration.objects.filter(user = u)
            #s = a_models.student_info.objects.get(user = u)
            data_dict = {'p':p, 'i':i, 'e':u.email, 'n':u.username, 'a':a_data}
            total_list.append(data_dict)
        except (a_models.profile.DoesNotExist, intern_registration.DoesNotExist, intern_data.DoesNotExist) as e:
            pass
    return render(request,'intern/list.html', {'list':total_list})

@login_required
@is_manager
def download_list(request):
    user_set = User.objects.all()
    total_list = []
    for u in user_set :
        try:
            p = a_models.profile.objects.get(user = u)
            a_data = intern_data.objects.get(user = u)
            i = intern_registration.objects.filter(user = u)
            #s = a_models.student_info.objects.get(user = u)
            data_dict = {'p':p, 'i':i, 'e':u.email, 'n':u.username, 'a':a_data,'s':s}
            total_list.append(data_dict)
        except (a_models.profile.DoesNotExist, intern_registration.DoesNotExist, intern_data.DoesNotExist) as e:
            pass
        response = HttpResponse(content_type='application/csv')
        response['Content-Disposition'] = 'attachment; filename=list.csv'
        wr = csv.writer(response)
        wr.writerow(['Date','Name','Email','Phone','Gender','College','Course','Username','Resume','Resume Link','Days','From','To','SOP','Intern'])
        for l in total_list:
            date1 = l['a'].updated_at
            name = l['p'].name
            email = l['e']
            phone = l['p'].phone
            gender = l['a'].gender
            college = l['p'].college
            course = l['a'].course
            u_name = l['n']
            resume = l['a'].resume
            resume_link = 'https://yuva.net.in/intern/resume_download/'+str(l['p'].user.id)
            days = l['a'].days
            from_date = l['a'].from_date
            to_date = l['a'].to_date
            sop = l['a'].sop
            intern = ''
            for li in l['i']:
                intern = intern+li.code.intern+' - '+li.code.field+' - '+li.reg_no+'|######|'
            data_list = [date1, name, email, phone, gender, college, course, u_name, resume,resume_link,days,from_date,to_date,sop, intern]
            wr.writerow(data_list)
    return response

@login_required
@is_manager
def resume_download(request,path):
    #file_path = os.path.join(settings.MEDIA_ROOT, path)
    #if os.path.exists(file_path):
    #    with open(file_path, 'rb') as fh:
    #        response = HttpResponse(fh.read(), content_type="application/resume.pdf")
    #        response['Content-Disposition'] = 'inline; filename=' + os.path.basename(file_path)
    #        return response
    #raise Http404
    user_obj = User.objects.get(id = path)
    p = profile.objects.get(user = user_obj)
    file = p.resume
    response = HttpResponse(FileWrapper(file), content_type='application/pdf')
    response['Content-Disposition'] = 'attachment; filename=resume.pdf'
    return response

