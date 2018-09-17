from django.shortcuts import render
from vimarsh18 import forms as v18_forms
from vimarsh18 import reg_no_generator
from account.views import messages
from django.shortcuts import redirect
from vimarsh18 import models as v18_models
from vimarsh18 import email_sender

# Create your views here.
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
