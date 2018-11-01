from django import forms
from vimarsh18 import models as v18
#from django.contrib.auth.forms import UserCreationForm, PasswordChangeForm
#from django.contrib.auth.models import User

year_choice = (
    ('','Select Course Year (currently studying)'),
    ('1','1'),
    ('2','2'),
    ('3','3'),
    ('4','4'),
    ('5','5'),
    )

ratings = (
    ('10', '10'),
    ('9', '9'),
    ('8', '8'),
    ('7', '7'),
    ('6', '6'),
    ('5', '5'),
    ('4', '4'),
    ('3', '3'),
    ('2', '2'),
    ('1', '1'),
    )

areaOfInterest = (
    ('','Select area of Interest'),
    ('Law and Polity', 'Law and Polity'),
                                  ('Science and Technology', 'Science and Technology'),
                                  ('Language Literature and Journalism', 'Language, Literature and Journalism'),
                                  ('General Awareness', 'General Awareness'))

pay_mode_choices = (
    ('',' Select Payment Method'),
    ('pay_online', 'Pay Online'),
    ('pay_venue','Will pay at venue during the time of Vimarsh')
    )

class volunteer_form(forms.ModelForm):
    course = forms.CharField(required=True, widget=forms.TextInput(attrs={'class':'form-control', 'placeholder':'Course'}))
    branch = forms.CharField(required=True, widget=forms.TextInput(attrs={'class':'form-control', 'placeholder':'Branch'}))
    year = forms.ChoiceField(choices=year_choice, required=True, widget=forms.Select(attrs={'class':'js-example-basic-single form-control', 'data-placeholder':'Select Course Year (currently studying)'}))
    interest = forms.ChoiceField(choices=areaOfInterest, required=True, widget=forms.Select(attrs={'class':'js-example-basic-single form-control', 'data-placeholder':'Select area of Interest'}))
    class Meta:
        model = v18.volunteer
        fields = {
            'course',
            'branch',
            'year',
            'interest',
            }

class multiple_choice_form(forms.Form):
    choice = forms.MultipleChoiceField(choices = areaOfInterest, required = True, widget  = forms.SelectMultiple(attrs={'class':'js-example-basic-multiple form-control', 'data-placeholder':'Select area of Interest'}))
    pay_choice = forms.ChoiceField(choices=pay_mode_choices, required=True, widget=forms.Select(attrs={'class':'js-example-basic-single form-control', 'data-placeholder':'Select Payment Method'}))

class single_field_form(forms.Form):
    field1 = forms.CharField()

class single_choice_form(forms.Form):
    pay_choice = forms.ChoiceField(choices=pay_mode_choices, required=True, widget=forms.Select(attrs={'class':'js-example-basic-single form-control', 'data-placeholder':'Select Payment Method'}))
    
class volunteer_certi_form(forms.Form):
    reg_no = forms.CharField(required=True, widget=forms.TextInput(attrs={'class':'form-control'}))
    email = forms.EmailField(required=True, widget=forms.TextInput(attrs={'class':'form-control'}))
    def clean_reg_no(self):
        reg_no = self.cleaned_data['reg_no'].upper()
        if not v18.volunteer.objects.filter(reg_no = reg_no).exists():
            raise forms.ValidationError('There is no volunteer with registration number '+reg_no+'. Please enter valid registration number')
        return reg_no

class feedback_form(forms.ModelForm):
    reg_no = forms.CharField(required=True, widget=forms.TextInput(attrs={'class':'form-control'}))
    content_use = forms.ChoiceField(choices=ratings, widget=forms.Select(attrs={'class':'form-control selectpicker', 'data-style':'btn btn-link'}))
    admin_satisfaction  = forms.ChoiceField(choices=ratings,  widget=forms.Select(attrs={'class':'form-control selectpicker', 'data-style':'btn btn-link'}))
    overall_satisfaction = forms.ChoiceField(choices=ratings,  widget=forms.Select(attrs={'class':'form-control selectpicker', 'data-style':'btn btn-link'}))
    comment = forms.CharField(required = False, widget=forms.Textarea(attrs={'class':'form-control', 'rows':'3'}))

    def clean_reg_no(self):
        reg_no = self.cleaned_data['reg_no'].upper()
        if not v18.participant.objects.filter(reg_no = reg_no).exists():
            raise forms.ValidationError('There is no participant with registration number '+reg_no+'. Please enter valid registration number')
        return reg_no

    class Meta:
        model = v18.feedback
        fields = {
            'reg_no',
            'content_use',
            'admin_satisfaction',
            'overall_satisfaction',
            'comment',
            }