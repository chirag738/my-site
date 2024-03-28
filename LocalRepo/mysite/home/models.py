from django.db import models

# Create your models here.
class Userlogin(models.Model):
    username = models.CharField(max_length=122)
    password = models.CharField(max_length=122)
    email = models.CharField(max_length=122)

class Report(models.Model):
    reporter_name = models.CharField(max_length=122)
    reporter_email = models.CharField(max_length=122)
    crime_desc = models.TextField()
    phone = models.CharField(max_length=122)
    date_of_report = models.DateField()

