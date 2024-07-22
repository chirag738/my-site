from django import forms
from home.models import YourDetail, CrimeDetail

class YourDetailsForm(forms.ModelForm):
    class Meta:
        model = YourDetail
        fields = ('first_name', 'middle_name', 'last_name', 'age', 'email_id', 'mobile_no', 'date', 'address')

class CrimeDetailsForm(forms.ModelForm):
    class Meta:
        model = CrimeDetail
        fields = ('case_id','criminal_name','nick_name','crime_type','criminal_age','crime_mob_no','date_of_crime','gender','crime_spot','clue','cs_status')
