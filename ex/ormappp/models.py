from django.db import models
from django.contrib import admin
class Bankloan (models.Model):
     acc=models.IntegerField(primary_key="acc")
     name=models.CharField(max_length=100)
     mobileno=models.IntegerField()
     pancode=models.IntegerField()
     aadharcode=models.IntegerField()
     
class BankloanAdmin(admin.ModelAdmin):
  list_display=('acc','name','mobileno','pancode','aadharcode')
