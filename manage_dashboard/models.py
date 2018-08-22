from django.db import models
from imagekit.models import ProcessedImageField
from imagekit.processors import ResizeToFill
from django.conf import settings

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
    fb_link = models.CharField(max_length = 200)
