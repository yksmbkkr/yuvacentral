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

areaOfInterest = (
    ('','Select area of Interest'),
    ('Law and Polity', 'Law and Polity'),
                                  ('Science and Technology', 'Science and Technology'),
                                  ('Language Literature and Journalism', 'Language, Literature and Journalism'),
                                  ('General Awareness', 'General Awareness'))

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