from django.db import models
from imagekit.models import ProcessedImageField
from imagekit.processors import ResizeToFill
from django.conf import settings
from django.contrib.auth.models import User


# Create your models here.
class up_events(models.Model):
    event_id = models.IntegerField(primary_key=True)
    pic = ProcessedImageField(upload_to = 'upcoming_events',
                               processors = [ResizeToFill(640,360)],
                               format = 'PNG',
                               options={'quality':50})
    name = models.CharField(max_length = 100)
    short_info = models.CharField(max_length = 500)
    date = models.CharField(max_length = 50)
    venue = models.CharField(max_length = 200)
    poc_name = models.CharField(max_length = 100)
    poc_number = models.CharField(max_length = 100)
    fb_link_status = models.BooleanField(default = False)
    fb_link = models.CharField(max_length = 200)
    reg_link_status = models.BooleanField(default = False)
    reg_link = models.CharField(max_length = 200)
    to_post = models.BooleanField(default = False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    class Meta:
        ordering = ['-created_at','-updated_at']

class vimarsh18_reciept(models.Model):
    number = models.CharField(max_length = 20, unique = True)
    status = models.BooleanField(default = False)
    creator = models.ForeignKey(User, on_delete=models.PROTECT, related_name = 'reciept_manager')
    used_by = models.ForeignKey(User, on_delete=models.PROTECT, related_name='reciept_user',null=True, default=None)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

