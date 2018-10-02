from django.db import models
from django.core.validators import RegexValidator
from django.contrib.auth.models import User
from django.core.validators import MinValueValidator

# Create your models here.

class user_check(models.Model):
    user = models.OneToOneField(User, on_delete = models.CASCADE, primary_key = True)
    email_confirmation_status = models.BooleanField(default = False)
    profile_status = models.BooleanField(default = False)
    manager_status = models.BooleanField(default = False)
    reciept_manager_status = models.BooleanField(default = False)
    profession = models.CharField(default = 'student', max_length = 20)

    def __str__(self):
        return self.user.username

class college_list_yuva(models.Model):
    college_id = models.IntegerField(primary_key=True)
    college_name = models.CharField(max_length = 500)

    def __str__(self):
        return self.college_name

    class Meta:
        ordering = ['college_name']

class profile(models.Model):
    user = models.OneToOneField(User, on_delete = models.CASCADE, primary_key = True)
    name = models.CharField(max_length=50, verbose_name ='Name')
    phone_regex = RegexValidator(regex=r'^\+?1?\d{9,10}$', message="Phone number must be entered in the format: '1234567890'. Up to 10 digits allowed.")
    phone= models.CharField(validators=[phone_regex], max_length=10, verbose_name ='Phone Number')
    college = models.ForeignKey(college_list_yuva,on_delete=models.PROTECT)
    def __str__(self):
        return self.user.username

class student_info(models.Model):
    user = models.OneToOneField(User, on_delete = models.CASCADE, primary_key = True)
    course = models.CharField(max_length=20)
    year = models.CharField(max_length=10)

    def __str__(self):
        return self.user.username


class other_info(models.Model):
    user = models.OneToOneField(User, on_delete = models.CASCADE, primary_key = True)
    designation = models.CharField(max_length=50)
    institution = models.CharField(max_length=200)

    def __str__(self):
        return self.user.username