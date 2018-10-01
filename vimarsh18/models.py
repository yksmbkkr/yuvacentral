from django.db import models
from django.contrib.auth.models import User

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

class participant(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)
    reg_no = models.CharField(max_length=10, unique=True)
    choice = models.CharField(max_length=100)

    def __str__(self):
        return self.user.username