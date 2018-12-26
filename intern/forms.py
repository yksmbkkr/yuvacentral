from django import forms
from intern.models import *
from django.contrib.auth.forms import UserCreationForm, PasswordChangeForm
from django.contrib.auth.models import User
from django.template.defaultfilters import filesizeformat
from django.utils.translation import ugettext_lazy as _
from django.conf import settings

law_choice = (
    ('Litigation','Litigation'),
    ('Corporate','Corporate'),
    ('Research','Research'),
    ('Judicial Internship','Judicial Internship'),
    ('Legal Aid/Prison','Legal Aid/Prison'),
    )

policy_choice = (
    ('National Security','National Security'),
    ('Women and Gender Studies','Women and Gender Studies'),
    ('International Relations','International Relations'),
    ('Indian Freedom Movement','Indian Freedom Movement'),
    ('Language and Ethnic Studies','Language and Ethnic Studies'),
    ('Education Policy','Education Policy'),
    )

social_choice = (
    ('Social Healthcare','Social Healthcare'),
    ('Slum Studies','Slum Studies'),
    ('Transgender and Red light area studies','Transgender and Red light area studies'),
    ('Refugee or Human Rights Studies','Refugee or Human Rights Studies'),
    ('Tribal Area Studies','Tribal Area Studies'),
    ('Village Development Programme','Village Development Programme'),
    ('Orphanages and old age homes','Orphanages and old age homes'),
    )

science_choice = (
    ('Physics','Physics'),
    ('Chemistry','Chemistry'),
    ('Biology','Biology'),
    ('Medical','Medical'),
    ('Engineering','Engineering'),
    )

media_choice = (
    ('Electronic Media','Electronic Media'),
    ('Online Media','Online Media'),
    ('Print media','Print media'),
    )

commerce_choice = (
    ('Commerce','Commerce'),
    ('Economics','Economics'),
    ('Finance','Finance'),
    )

gender = (
    ('Female','Female'),
    ('Male','Male'),
    )


class intern_data_form(forms.ModelForm):
    course = forms.CharField(label = 'Course', widget=forms.TextInput(attrs={'class':'form-control','placeholder':'Course...'}), required = True)
    gender = forms.ChoiceField(label = 'Gender', choices = gender, required = True, widget=forms.Select(attrs={'class':'form-control', 'title':'Gender'}))
    sop = forms.CharField(label = 'Write SOP of Approx 250 Words', required = True, widget = forms.Textarea(attrs = {'class':'form-control','placeholder':'Write SOP of Approx 250 Words'}))
    resume = forms.FileField()
    from_date = forms.DateField(label = 'Prefered starting date of Internship', widget=forms.TextInput(attrs={'class':'form-control datepicker','placeholder':'Prefered starting date'}), required = True)
    to_date = forms.DateField(label = 'Prefered end date of Internship', widget=forms.TextInput(attrs={'class':'form-control datepicker','placeholder':'Prefered end date'}), required = True)
    days = forms.CharField(label = 'Days', widget=forms.TextInput(attrs={'class':'form-control','placeholder':'Prefered no of days'}), required = True)


    def clean_resume(self):
            resume = self.cleaned_data['resume']
            content_type = resume.content_type.split('/')[1]
            if content_type in settings.CONTENT_TYPES:
                if resume._size > settings.MAX_UPLOAD_SIZE:
                    raise forms.ValidationError(_('Please keep filesize under %(permitsize)s. Current filesize %(thissize)s'), code='InvalidFileSize', params ={'permitsize' : filesizeformat(settings.MAX_UPLOAD_SIZE), 'thissize':filesizeformat(resume._size)},)
            else:
                raise forms.ValidationError(_('File type is not supported. Only PDF supported.'), code = 'InvalidFileType',)
            return resume

    class Meta:
        model = intern_data

        fields = (
            'course',
            'gender',
            'resume',
            'sop',
            'days',
            'from_date',
            'to_date',
            )


