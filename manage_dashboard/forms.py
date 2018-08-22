from django import forms
from django.contrib.auth.models import User
from manage_dashboard import  models as m_models

class upcoming_events_form(forms.ModelForm):
    pic = forms.ImageField(required = True, label='Select Cover Pic 640*360', widget = forms.ClearableFileInput(attrs={'class':'custom-file-input'}))
    name = forms.CharField(required=True,label='Name of Event', widget=forms.TextInput(attrs={'class':'form-control', 'placeholder':'Name of Event'}))
    short_info = forms.CharField(required=True,label= 'Info of Event', widget=forms.Textarea(attrs={'class':'form-control', 'rows':'5'}))
    date = forms.CharField(required=True,label='Date of Event', widget=forms.TextInput(attrs={'class':'form-control', 'placeholder':'Date of Event'}))
    venue = forms.CharField(required=True,label= 'Venue', widget=forms.Textarea(attrs={'class':'form-control', 'rows':'3'}))
    poc_name = forms.CharField(required=True,label='Name of POC', widget=forms.TextInput(attrs={'class':'form-control', 'placeholder':'Name of POC'}))
    poc_number = forms.CharField(required=True,label='Number of POC', widget=forms.TextInput(attrs={'class':'form-control', 'placeholder':'Number of POC'}))
    fb_link = forms.CharField(required=True,label='FB Link', widget=forms.TextInput(attrs={'class':'form-control', 'placeholder':'FB Link', 'value':'https://fb.com/'}))

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
            'fb_link',
            )

