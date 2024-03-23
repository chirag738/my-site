from django.contrib import admin
from home.models import Report, Userlogin

#username - admin, password - admin

# Register your models here.
admin.site.register(Report)
admin.site.register(Userlogin)
