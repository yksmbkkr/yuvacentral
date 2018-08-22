from django import forms
from django.contrib.auth.forms import UserCreationForm, PasswordChangeForm
from django.contrib.auth.models import User
from django.template.defaultfilters import filesizeformat
from django.utils.translation import ugettext_lazy as _
from django.conf import settings
from account import models as a_models


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
    college = forms.ModelChoiceField(a_models.college_list_yuva.objects.all(),empty_label='Select College', required=True, widget=forms.Select(attrs={'class':'form-control selectpicker show-tick','data-live-search':'true','data-style':'btn-primary','style':'width:fit !important;'}))
    class Meta:
        model = a_models.profile
        fields = ('name', 'phone', 'college',)
