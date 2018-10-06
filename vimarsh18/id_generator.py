import qrcode
from django.shortcuts import Http404
from vimarsh18 import models as v18_models
from django.core.files.base import ContentFile
from io import BytesIO

def try_qr(user = None):
    if user==None:
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
    return img
