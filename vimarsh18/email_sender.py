from django.core.mail import send_mail, get_connection
from django.core.mail import EmailMultiAlternatives
from django.template.loader import get_template
from django.template import Context
#con = get_connection('django.core.mail.backends.smtp.EmailBackend')

def volunteer_email(user = None):
    plaintext = get_template('emails/volunteer_email.txt')
    htmly = get_template('emails/volunteer_email.html')
    fail_silently=False
    d = { 'name': user.profile.name, 'phone':user.profile.phone, 'email':user.email, 'college':user.profile.college,'course':user.volunteer.course,'branch':user.volunteer.branch,'year':user.volunteer.year,'reg_no':user.volunteer.reg_no, 'interest': user.volunteer.interest}
    subject, from_email = 'Volunteer Registration Notification - Vimarsh 2018', 'Vimarsh - YUVA <vimarsh@yuva.net.in>'
    to = [str(user.email),]
    text_content = plaintext.render(d)
    html_content = htmly.render(d)
    msg = EmailMultiAlternatives(subject, text_content, from_email, to)
    msg.attach_alternative(html_content, "text/html")
    msg.send(fail_silently=False)            