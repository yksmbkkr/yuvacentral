from django.db import models
from django.core.validators import MinValueValidator
from django.contrib.auth.models import User

# Create your models here.
def user_directory_path(instance, filename):
         return 'intern/user_{0}/{1}'.format(instance.user.username, filename)

class intern_data(models.Model):
        course = models.CharField(max_length=20, verbose_name ='Course', default = 'NA')
        gender = models.CharField(max_length=10, verbose_name ='Gender')
        resume = models.FileField(upload_to=user_directory_path, null = True)
        sop = models.TextField()
        days = models.PositiveIntegerField(default = 30,  validators=[MinValueValidator(1)])
        from_date = models.DateField(null = True)
        to_date = models.DateField(null = True)
        user = models.OneToOneField(User, on_delete = models.CASCADE, primary_key = True)
        updated_at = models.DateTimeField(auto_now=True)
        class Meta:
            ordering = ['updated_at']

class intern_code(models.Model):
    code = models.CharField(max_length = 50, primary_key = True)
    field = models.CharField(max_length = 50)
    intern = models.CharField(max_length = 50)
    def __str__(self):
            return self.code


class intern_registration(models.Model):
    code = models.ForeignKey(intern_code, on_delete=models.CASCADE)
    reg_no = models.CharField(default = 'null', max_length = 10)
    user = models.ForeignKey(User, on_delete = models.CASCADE)
    updated_at = models.DateTimeField(auto_now=True)
    class Meta:
        ordering = ['updated_at']