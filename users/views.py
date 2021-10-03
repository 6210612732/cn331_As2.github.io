from django.contrib.auth import authenticate, login ,logout
from django.contrib.auth.models import User
from django.shortcuts import render, redirect
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.contrib import messages
from django.http import HttpResponse
from users.models import Student
# Create your views here.


def index(request):
    #messages.info(request,'fesf')
    if not request.user.is_authenticated:
        #return HttpResponseRedirect(reverse("users:login"))
        return render(request, "users/login.html")
    else:
        return HttpResponseRedirect(reverse("regis:home"))




def login_view(request):
    #messages.info(request,'asd')
    if request.method=="POST":
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username=username,password=password)
        if user is not None:
            login(request, user)
            #messages.info(request,'ยินดีต้อนรับ')
            return redirect('/regis/')
        else:
            requery = User.objects.all().filter(username = username)
            if requery.values_list('id'):
                messages.info(request,'รหัสผ่านไม่ถูกต้อง')
                #return redirect('/users/login/')

            else:
                messages.info(request,'ไม่มีชื่อผู้ใช้นี้')
                #return redirect('/users/login/')
    #return redirect('/users/login/')
    return redirect('/users/')
    #return HttpResponseRedirect(reverse("users:login"))


def logout_view(request):
    #messages.info(request,'รหัสผ่านไม่ถูกต้อง')
    logout(request)
    return render(request, "users/login.html")


def wel(request):
    return render(request, "users/welcome.html")


def signup(request):
    return render(request, "users/signup.html")

"""
def adduser(request):
  #  ausername=request.POST['a1']
  #  aemail=request.POST['a2']
  #  apassword=request.POST['a3']
  #  arepassword=request.POST['a4']
    check = 1
    message = ""
    ausername=request.POST.get('a1', False);
    aemail=request.POST.get('a2', False);
    apassword=request.POST.get('a3', False);
    arepassword=request.POST.get('a4', False);
    first=request.POST.get('a5', False);
    last=request.POST.get('a6', False);
    year=request.POST.get('a7', False);

#    te = Student.objects.all().filter(username=ausername)

#    if te :
#        check = 0
#        message = "username already exists"
#        messages.info(request,message)

    if apassword != arepassword :
        check = 0
        message = "pass and repass doesn't match"
        messages.info(request,message)

    if check == 1 :
        user = User.objects.create_user('ausername', 'aemail', 'apassword')
        tempp = Student.objects.all().filter(username=ausername)
        temp2 = tempp.values_list('id')
        temp3 = int(temp2[0][0])
   #     adder = Student(STID=temp3,
   #             college_year=year,
   #             Gpax=0,
   #             )
   #     adder.save()
        messages.info(request,'เพิ่มผู้ใช้สำเร็จ')
        return redirect('login',)
    else :
        return redirect('login')
"""