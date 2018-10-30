from PIL import Image, ImageDraw, ImageFont
from io import BytesIO, StringIO
from django.template.loader import get_template
from django.core.mail import EmailMultiAlternatives

def format_name(name):
    nlist = name.split(' ')
    str1 = ''
    i=0
    for n in nlist:
        if i >= 3 :
            return str1
        str1 = str1 + n +' '
        i = i+1
    return str1

def p_create(name, email,reg_no):
    name = format_name(name)
    bg_url = '/home/adminyash/yuvacentral/vimarsh18/static/icard/bgp.png'
    #bg_url = 'C:/Users/Yash Kulshreshtha/source/repos/yuvacentral/yuvacentral/vimarsh18/static/icard/bgp.png'
    font = ImageFont.truetype(font='/home/adminyash/yuvacentral/vimarsh18/static/icard/calibri.ttf',size = 22)
    #font = ImageFont.truetype(font='C:/Users/Yash Kulshreshtha/source/repos/yuvacentral/yuvacentral/vimarsh18/static/icard/calibri.ttf',size = 22)
    bg = Image.open(bg_url)
    draw =  ImageDraw.Draw(bg)
    img_io = BytesIO()
    draw.text((490,225),name.upper(),fill = (36,99,177), font = font)
    bg.save(img_io, 'PNG')

    #################EMAIL#############################
    plaintext = get_template('emails/certi.txt')
    htmly = get_template('emails/certi.html')
    fail_silently=False
    d = {'name':name}
    subject, from_email = 'Participation Certificate - Vimarsh 2018', 'Vimarsh - YUVA <vimarsh@yuva.net.in>'
    to = [str(email),]
    text_content = plaintext.render(d)
    html_content = htmly.render(d)
    msg = EmailMultiAlternatives(subject, text_content, from_email, to)
    msg.attach_alternative(html_content, "text/html")
    img_io_get = img_io.getvalue()
    msg.attach(reg_no+'.png', img_io_get, 'image/png')
    msg.send(fail_silently=False)  
    #################EMAIL CLOSE########################
    bg.close()
