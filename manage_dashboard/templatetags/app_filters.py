from django import template
from datetime import date, timedelta

register = template.Library()

@register.filter(name='get_vimarsh_day')
def get_vimarsh_day(value):
    value = str(value)
    value = value + ' October'
    return value

@register.filter(name='get_vimarsh_domain')
def get_vimarsh_domain(value):
    if value == 'law_and_polity':
        return 'Law and Polity'
    elif value == 'science_and_technology':
        return 'Science and Technology'
    elif value == 'language_literature_and_journalism':
        return 'Language, Literature and Journalism'
    else :
        return 'General Awareness'