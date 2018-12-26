from django.utils import timezone    
from io import BytesIO
from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import letter




def generate_pdf(request,d,html_content,text_content):
    y = 700
    buffer = BytesIO()
    p = canvas.Canvas(buffer, pagesize=letter)
    p.setFont('Helvetica', 14)
    textObj = p.beginText(80, y)
    textObj.textLines(text_content)
    p.drawText(textObj)
    #p.drawString(20, y, pdf_content)
    
    #p.drawText(pdf_content)
    p.showPage()
    p.save()
    pdf = buffer.getvalue()
    buffer.close()
    
    return pdf
