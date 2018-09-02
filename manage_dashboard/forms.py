from django import forms
from django.contrib.auth.models import User
from manage_dashboard import  models as m_models

boolean_choices = (
    (False,'No'),
    (True,'Yes')
    
    )

class upcoming_events_form(forms.ModelForm):
    pic = forms.ImageField(required = True, label='Select Cover Pic 640*360', widget = forms.ClearableFileInput(attrs={'class':'custom-file-input'}))
    name = forms.CharField(required=True,label='Name of Event', widget=forms.TextInput(attrs={'class':'form-control', 'placeholder':'Name of Event'}))
    short_info = forms.CharField(required=True,label= 'Info of Event', widget=forms.Textarea(attrs={'class':'form-control', 'rows':'5'}))
    date = forms.CharField(required=True,label='Date of Event', widget=forms.TextInput(attrs={'class':'form-control', 'placeholder':'Date of Event'}))
    venue = forms.CharField(required=True,label= 'Venue', widget=forms.Textarea(attrs={'class':'form-control', 'rows':'3'}))
    poc_name = forms.CharField(required=True,label='Name of POC', widget=forms.TextInput(attrs={'class':'form-control', 'placeholder':'Name of POC'}))
    poc_number = forms.CharField(required=True,label='Number of POC', widget=forms.TextInput(attrs={'class':'form-control', 'placeholder':'Number of POC'}))
    fb_link_status = forms.CharField(label='Show FB Link', widget=forms.Select(choices=boolean_choices, attrs={'class':'form-control'}))
    fb_link = forms.CharField(required=True,label='FB Link (leave empty if not required)', widget=forms.TextInput(attrs={'class':'form-control', 'placeholder':'FB Link', 'value':'https://fb.com/'}))
    reg_link_status = forms.CharField(label='Show Registration Link', widget=forms.Select(choices=boolean_choices, attrs={'class':'form-control'}))
    reg_link = forms.CharField(label='Registration Link (leave empty if not required)', widget=forms.TextInput(attrs={'class':'form-control', 'placeholder':'Registration Link'}))

    class Meta:
        model = m_models.up_events
        fields = (
            'pic',
            'name',
            'short_info',
            'date',
            'venue',
            'poc_name',
            'poc_number',
            'fb_link_status',
            'fb_link',
            'reg_link_status',
            'reg_link',
            )

