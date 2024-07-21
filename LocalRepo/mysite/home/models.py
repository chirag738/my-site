from django.db import models
from django.contrib.auth.models import User 
from django import forms

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
    def __str__(self):
        return self.first_name

class CrimeDetail(models.Model):
    class Meta:
        permissions = (            
            ('can_create_crime_report', 'Can create crime report'),
            ('can_update_crime_report', 'Can update crime report'),
            ('can_delete_crime_report', 'Can delete crime report'),
        )
    case_id = models.CharField(max_length=10, unique=True, default=123456)
    criminal_name = models.CharField(max_length=100)
    nick_name = models.CharField(max_length=100)
    crime_type = models.CharField(max_length=100)
    criminal_age = models.IntegerField()
    crime_mob_no = models.IntegerField()
    date_of_crime = models.DateField()
    gender = models.CharField(max_length=100)
    crime_spot = models.TextField()
    clue = models.TextField()
    cs_status = models.CharField(max_length=100)
    def __str__(self):
        return self.criminal_name

class YourDetailForm(forms.ModelForm):
    class Meta:
        model = YourDetail
        fields = ('first_name','middle_name','last_name','age','email_id','mobile_no','date','address')

class CrimeDetailForm(forms.ModelForm):
    class Meta:
        model = CrimeDetail
        fields = ('case_id','criminal_name','nick_name','crime_type','criminal_age','crime_mob_no','date_of_crime','gender','crime_spot','clue','cs_status')
