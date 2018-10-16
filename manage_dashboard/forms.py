from django import forms
from django.contrib.auth.models import User
from manage_dashboard import  models as m_models
from vimarsh18 import models as v18_models
from django.utils.safestring import mark_safe

boolean_choices = (
    (False,'No'),
    (True,'Yes')
    )

id_card_choice = (
    ('guest','Guest'),
    ('organiser','Organizer'),
    ('volunteer_guest','Volunteer managing dignitaries')
    )

areaOfInterest = (
    ('','Select area of Interest'),
    ('law_and_polity', 'Law and Polity'),
                                  ('science_and_technology', 'Science and Technology'),
                                  ('language_literature_and_journalism', 'Language, Literature and Journalism'),
                                  ('general_awareness', 'General Awareness'))

day_choice = (
    ('', 'Select Day'),
    ('22', 'October 22'),
    ('23', 'October 23'),
    ('24', 'October 24')
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

class CustomFileWidget(forms.FileInput):
    """
    A FileField Widget that shows its current value if it has one.
    """
    def __init__(self, attrs={}):
        super(CustomFileWidget, self).__init__(attrs)

    def render(self, name, value, attrs=None):
        output = []
        if value and hasattr(value, "url"):
            output.append('</div>%s <a target="_blank" href="%s">%s</a> <br />%s <div class="custom-file">' % \
                ('Currently:', value.url, value, 'Change:'))
        output.append(super(CustomFileWidget, self).render(name, value, attrs))
        return mark_safe(u''.join(output))

class speaker_form(forms.ModelForm):
    pic = forms.ImageField(required = True, label='Select Cover Pic 400*400', widget = CustomFileWidget(attrs={'class':'custom-file-input'}))
    name = forms.CharField(required=True,label='Name', widget=forms.TextInput(attrs={'class':'form-control', 'placeholder':'Name'}))
    info = forms.CharField(required=True,label= 'Info', widget=forms.Textarea(attrs={'class':'form-control', 'rows':'5'}))

    class Meta:
        model = v18_models.speaker
        fields = ('pic','name','info')

class session_vim_form(forms.ModelForm):
    topic = forms.CharField(required=True, label='Topic', widget=forms.TextInput(attrs={'class':'form-control', 'placeholder':'Topic'}))
    info = forms.CharField(required=True,label= 'Info', widget=forms.Textarea(attrs={'class':'form-control', 'rows':'5'}))
    day = forms.CharField(label='Day', widget=forms.Select(choices=day_choice, attrs={'class':'form-control'}))
    domain = forms.CharField(label='Domain', widget=forms.Select(choices=areaOfInterest, attrs={'class':'form-control'}))
    start_time = forms.TimeField(label = 'Start Time', widget=forms.TextInput(attrs={'class':'form-control', 'placeholder':'Start Time'}))
    end_time = forms.TimeField(label = 'End Time', widget=forms.TextInput(attrs={'class':'form-control', 'placeholder':'End Time'}))
    class Meta:
        model = v18_models.session_vim
        fields = ('topic', 'info', 'day', 'domain', 'start_time', 'end_time')

class id_choice_form(forms.Form):
    id_type = forms.CharField(required = True, label='Select Type of ICard', widget=forms.Select(choices=id_card_choice, attrs={'class':'form-control'}))
    name = forms.CharField(required=True, label='Name', widget=forms.TextInput(attrs={'class':'form-control', 'placeholder':'Name'}))