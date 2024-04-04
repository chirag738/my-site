from django.db import models


# Create your models here.
class YourDetail(models.Model):
    first_name = models.CharField(max_length=100)
    middle_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    age = models.IntegerField()
    email_id = models.CharField(max_length=100)
    mobile_no = models.IntegerField()
    date = models.DateField()
    address = models.TextField()

class CrimeDetail(models.Model):
    criminal_name = models.CharField(max_length=100)
    nick_name = models.CharField(max_length=100)
    crime_type = models.CharField(max_length=100)
    criminal_age = models.IntegerField()
    crime_mob_no = models.IntegerField()
    date_of_crime = models.DateField()
    gender = models.CharField(max_length=100)
    crime_spot = models.TextField()
    clue = models.TextField()
