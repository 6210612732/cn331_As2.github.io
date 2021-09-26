from django.http import HttpResponseRedirect
from django.urls import reverse
from django.shortcuts import redirect, render
from django.contrib.auth.models import User,auth


# Create your views here.


from .models import Course
from users.models import Student
def index(request):
    #data_student = Student.objects.get(pk=2)
    #non_course = Course.objects.exclude(enroll=data_student).all  #show all of courses that member doesnt enroll
    #return render(request, "regis/mysub.html" , {'courses':non_course})
    a1=''
    a2=0
    a1=request.POST.get('a1', '');
    a2=request.POST.get('a2', 0);
    temp3 = 0
    year = 0
    temp = User.objects.all().filter(id=request.user.id)
    temp4 = Student.objects.all().filter(STID=request.user.id)
    temp2 = temp4.values_list('college_year')
    if temp2: 
        temp3 = int(temp2[0][0])
    if temp3:
        year = temp3
        data = Course.objects.exclude(student=request.user.id).filter(for_year=year)
    else:
        data = Course.objects.exclude(student=request.user.id) #.filter(year=year[0][0]) # เอาช่อง isstaffเก็บชั้นปีละกัน
    data2 = Course.objects.all()
    if a2!= '0' and a1 != '':
       data2 = Course.objects.all().filter(c_code=a1,for_year=a2)
    elif a2!='0':
       data2 = Course.objects.all().filter(for_year=a2)
    elif a1 != '':
       data2 = Course.objects.all().filter(c_code=a1)


    return render(request, "regis/index.html",{'courses':data,"data2":data2,"year":year,"a1":a1,"a2":a2})


def mysub(request):
    data = Course.objects.filter(student=request.user.id)
    return render(request, "regis/mysub.html",{'courses':data})



def regis(request, course_id):
    course = Course.objects.get(pk=course_id)
    if request.user not in course.student.all():
         course.student.add(request.user)
         course.number_of_Applicants += 1
         course.save()
         return redirect('/regis')
    return redirect('/regis')

def cancel(request, course_id, ffrom):
    course = Course.objects.get(pk=course_id)
    if request.user in course.student.all():
         course.student.remove(request.user)
         course.number_of_Applicants -= 1
         course.save()
         if(ffrom==1):
            return redirect('/regis/mysub')
         else:
            return redirect('/regis')
    return redirect('/regis')

def course(request,course_id):
    status = 0
    course = Course.objects.all().filter(id=course_id)
    check = Course.objects.get(pk=course_id)
    if request.user in check.student.all():
        status = 1
    return render(request, "regis/course.html",{"course":course,"status":status})

#return render(request, "regis/mysub.html" , {'courses':non_course})
#return render(request, "regis/mysub.html" , {'courses':data_course})

# เหมือนว่ากล่องจะpaddingมากไป







