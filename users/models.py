from django.db import models

# Create your models here.
class Student(models.Model):
    STID = models.IntegerField()
    tel = models.CharField(max_length=20)
    college_year = models.IntegerField()
    gender = models.CharField(max_length=10)
    birth_date = models.CharField(max_length=10)
    blood_type = models.CharField(max_length=2)
    date = models.DateField()
    Gpax = models.FloatField()
    