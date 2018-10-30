from django.db import models
from django.contrib.auth.models import User
from imagekit.models import ProcessedImageField
from imagekit.processors import ResizeToFill

# Create your models here.

class volunteer(models.Model):
    #areaOfInterest = (('Law and Polity', 'Law and Polity'),
    #                              ('Science and Technology', 'Science and Technology'),
    #                              ('Language Literature and Journalism', 'Language, Literature and Journalism'),
    #                              ('General Awareness', 'General Awareness'))
    user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)
    reg_no = models.CharField(max_length=10, unique=True)
    course = models.CharField(max_length=20)
    branch = models.CharField(max_length=20)
    year = models.CharField(max_length=10)
    interest = models.CharField(max_length=50)
    
    def __str__(self):
        return self.user.username

class qr_code_reg(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)
    qr_code = models.ImageField(upload_to = 'qr_codes', null = True)
    def __str__(self):
        return self.user.username

class id_card(models.Model):
    reg_no = models.CharField(max_length = 10)
    name = models.CharField(max_length = 50)
    id_img = models.ImageField(upload_to = 'id_cards', null = True)
    def __str__(self):
        return self.reg_no

    class Meta:
        ordering = ['reg_no']

class participant(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)
    reg_no = models.CharField(max_length=15, unique=True)
    choice = models.CharField(max_length=200)
    pay_mode = models.CharField(max_length = 20, default = 'pay_venue')
    payment_status = models.BooleanField(default = False)

    def __str__(self):
        return self.user.username

class speaker(models.Model):
    pic = ProcessedImageField(upload_to = 'vimarsh18_speakers',
                               processors = [ResizeToFill(400,400)],
                               format = 'PNG',
                               options={'quality':50})
    name = models.CharField(max_length = 50, blank = True)
    info = models.CharField(max_length = 250, blank = True)

    def __str__(self):
        return self.name

    class Meta:
        ordering = ['name']

class session_vim(models.Model):
    sid = models.CharField(max_length = 10, primary_key = True)
    topic = models.CharField(max_length = 250)
    info = models.CharField(max_length = 350)
    day = models.CharField(max_length = 2)
    domain = models.CharField(max_length = 100)
    start_time = models.TimeField()
    end_time = models.TimeField()

    def __str__(self):
        return self.sid
    class Meta:
        ordering = ['day','start_time','end_time']

class attendance(models.Model):
    rid = models.CharField(max_length = 20)
    sid = models.ForeignKey(session_vim, on_delete = models.CASCADE)
    user = models.ForeignKey(User, on_delete = models.CASCADE)

class venue_payment_stats(models.Model):
    collector = models.ForeignKey(User, on_delete = models.PROTECT)
    payee_id = models.CharField(max_length = 20)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    class Meta:
        ordering = ['-created_at']

class id_special(models.Model):
    name = models.CharField(max_length = 100)
    id_img = models.ImageField(upload_to = 'id_cards_special', null = True)
    def __str__(self):
        return self.name

class hardcopy(models.Model):
    user = models.OneToOneField(User, on_delete = models.CASCADE)
    reg_no = models.CharField(max_length = 20)
    def __str__(self):
        return self.reg_no

class feedback(models.Model):
    user = models.OneToOneField(User, on_delete = models.CASCADE)
    reg_no = models.CharField(verbose_name='Registration Number', max_length = 20)
    content_use = models.CharField(max_length = 5, default = 'NA')
    admin_satisfaction = models.CharField(max_length = 5, default = 'NA')
    overall_satisfaction = models.CharField(max_length = 5, default = 'NA')
    comment = models.CharField(max_length = 1000, default = 'NA')
    def __str__(self):
        return self.reg_no