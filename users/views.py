from django.contrib.auth import authenticate, login ,logout
from django.contrib.auth.models import User
from django.shortcuts import render, redirect
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.contrib import messages
from django.http import HttpResponse
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

