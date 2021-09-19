from django.db import models
from django.contrib.auth.models import User

# Create your models here.

# User     1 zwaapalm
#          2 tabong


class Term(models.Model):   # 1 physics
    semeter =  models.IntegerField()
    year = models.IntegerField()
    

    def __str__(self):
        return f"{self.semeter}/{self.year}"

class Course(models.Model):
    c_name = models.CharField(max_length=200)
    c_code = models.CharField(max_length=10)
    number_of_Applicants = models.IntegerField(default=0)
    seat = models.IntegerField()
    status = models.IntegerField(null=True)
    semeter = models.ForeignKey(Term,on_delete=models.CASCADE,related_name="c_term")
    student =  models.ManyToManyField(User, blank=True,related_name="student")
    for_year = models.IntegerField(null=True)
    year = models.IntegerField(null=True)
  
    
    def __str__(self):
        return f"{self.c_name}"





