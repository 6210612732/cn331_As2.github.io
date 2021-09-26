from django.db import models

# Create your models here.
class Student(models.Model):
    STID = models.IntegerField()
    tel = models.CharField(max_length=20, null=True)
    college_year = models.IntegerField(null=True)
    gender = models.CharField(max_length=10,null=True)
    birth_date = models.CharField(max_length=10,null=True)
    blood_type = models.CharField(max_length=2,null=True)
    date = models.DateField(null=True)
    Gpax = models.FloatField(null=True)
    