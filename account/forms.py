from django import forms
from django.contrib.auth.forms import UserCreationForm, PasswordChangeForm
from django.contrib.auth.models import User
from django.template.defaultfilters import filesizeformat
from django.utils.translation import ugettext_lazy as _
from django.conf import settings
from account import models as a_models

prof_choice = (
    ('','Select profession'),
    ('student','Student'),
    ('teaching','Teacher/Professor'),
    ('other','Others')
    )

class single_field_form(forms.Form):
    field1 = forms.CharField()

class profession_choice_form(forms.Form):
    profession =  forms.ChoiceField(choices=prof_choice, required=True, widget=forms.Select(attrs={'class':'js-example-basic-single form-control', 'data-placeholder':'Select'}))
    


class registration_form(UserCreationForm):
    username = forms.CharField(max_length=30, required=True, widget=forms.TextInput(attrs={'class':'form-control', 'placeholder':'Username'}))
    email = forms.EmailField(max_length=254, required=True, help_text='Required. Inform a valid email address.', widget=forms.TextInput(attrs={'class':'form-control', 'placeholder':'Email'}))
    password1 = forms.CharField(widget=forms.PasswordInput(attrs={'class':'form-control', 'placeholder':'Password'}))
    password2 = forms.CharField(widget=forms.PasswordInput(attrs={'class':'form-control', 'placeholder':'Retype Password'}))

    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2', )

class profile_form(forms.ModelForm):
    name = forms.CharField(max_length=30, required=True, widget=forms.TextInput(attrs={'class':'form-control', 'placeholder':'Name'}))
    phone = forms.CharField(max_length=30, required=True, widget=forms.TextInput(attrs={'class':'form-control', 'placeholder':'Phone Number'}))
    college = forms.ModelChoiceField(a_models.college_list_yuva.objects.all(),empty_label='Select College', required=True, widget=forms.Select(attrs={'class':'js-example-basic-single form-control', 'data-placeholder':'Select College'}))
    class Meta:
        model = a_models.profile
        fields = ('name', 'phone', 'college',)

class student_info_form(forms.ModelForm):
    course = forms.CharField()
    year = forms.CharField()
    class Meta:
        model = a_models.student_info
        fields = ('course', 'year',)

class other_info_form(forms.ModelForm):
    designation = forms.CharField()
    institution = forms.CharField()
    class Meta:
        model = a_models.student_info
        fields = ('designation', 'institution',)