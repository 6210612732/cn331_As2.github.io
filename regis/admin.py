from django.contrib import admin

# Register your models here.
from .models import  Term, Course

admin.site.register(Term)
admin.site.register(Course)
