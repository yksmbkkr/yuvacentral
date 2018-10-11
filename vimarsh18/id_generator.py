import qrcode
from django.shortcuts import Http404
from vimarsh18 import models as v18_models
from django.core.files.base import ContentFile
from io import BytesIO, StringIO
from django.contrib.staticfiles.templatetags.staticfiles import static
from PIL import Image, ImageDraw, ImageFont
from django.contrib.staticfiles.storage import staticfiles_storage
import os
from django.conf import settings
import urllib

def try_qr(user = None):
    if v18_models.qr_code_reg.objects.filter(user=user).count() > 0:
        #print('already exists')
        raise Http404
    if user==None:
        #print('no user')
        raise Http404
    reg_no = user.participant.reg_no
    qr = qrcode.QRCode(
        error_correction=qrcode.constants.ERROR_CORRECT_Q,
        box_size=5,
        border=1,
        )
    qr.add_data(reg_no)
    qr.make(fit=True)
    img = qr.make_image(fill_color="black", back_color="white")
    qr_obj = v18_models.qr_code_reg(user = user)
    filename = reg_no+'.png'
    img_io = BytesIO()
    img.save(img_io, img.format, quality=50)
    qr_obj.qr_code.save(filename, ContentFile(img_io.getvalue()), save=False)
    qr_obj.save()

def participant_student_id(reg_no = None):
    if v18_models.id_card.objects.filter(reg_no=reg_no).count() > 0:
        return
    if reg_no == None:
        #print("No reg_no")
        raise Http404
    try:
        p_obj = v18_models.participant.objects.get(reg_no = reg_no)
    except v18_models.participant.DoesNotExist:
        #print("participant not exist")
        raise Http404
    name = p_obj.user.profile.name
    #bg_url = 'C:/Users/Yash Kulshreshtha/source/repos/yuvacentral/yuvacentral/vimarsh18/static/icard/ps.png'
    #bg_url = StringIO(urllib.request.urlopen(static('icard/ps.png')).read())
    profession = p_obj.user.user_check.profession
    if profession == 'student':
        bg_url = '/home/adminyash/yuvacentral/vimarsh18/static/icard/ps.png'
        #bg_url = 'C:/Users/Yash Kulshreshtha/source/repos/yuvacentral/yuvacentral/vimarsh18/static/icard/ps.png'
    elif profession == 'teaching':
        bg_url = '/home/adminyash/yuvacentral/vimarsh18/static/icard/pt.png'
        #bg_url = 'C:/Users/Yash Kulshreshtha/source/repos/yuvacentral/yuvacentral/vimarsh18/static/icard/pt.png'
    else:
        bg_url = '/home/adminyash/yuvacentral/vimarsh18/static/icard/po.png'
        #bg_url = 'C:/Users/Yash Kulshreshtha/source/repos/yuvacentral/yuvacentral/vimarsh18/static/icard/po.png'
    bg = Image.open(bg_url)
    if v18_models.qr_code_reg.objects.filter(user=p_obj.user).count() < 1:
        try_qr(p_obj.user)
    else:
        pass
    qr_url = p_obj.user.qr_code_reg.qr_code
    qr = Image.open(qr_url)
    filename = reg_no+'.png'
    img_io = BytesIO()
    draw =  ImageDraw.Draw(bg)
    font = ImageFont.truetype(font='/home/adminyash/yuvacentral/vimarsh18/static/icard/calibri.ttf',size = 22)
    #font = ImageFont.truetype(font='C:/Users/Yash Kulshreshtha/source/repos/yuvacentral/yuvacentral/vimarsh18/static/icard/calibri.ttf',size = 22)
    draw.text((60,310),name.replace(' ','\n')[:40]+'\n'+'\n'+reg_no,fill = (1,72,174), font = font)
    bg.paste(qr,(260,350))
    bg.save(img_io, bg.format, quality=50)
    id_obj = v18_models.id_card(reg_no=reg_no, name = name)
    id_obj.id_img.save(filename, ContentFile(img_io.getvalue()), save=False)
    id_obj.save()