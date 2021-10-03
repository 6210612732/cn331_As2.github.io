
from django.test import TestCase, Client
from django.urls import reverse
from django.contrib.auth.hashers import make_password
from django.contrib.auth.models import User,auth
from regis.models import Course
from users.models import Student
from django.http import HttpResponseRedirect
from django.shortcuts import redirect, render


password = make_password('1234')
# Create your tests here.

class ProjectTestRespond_users(TestCase):
    def setUp(self):
        user1 = User.objects.create(username='user1', password=password, email='user1@example.com',is_superuser=True)
        user2 = User.objects.create(username='user2', password=password, email='user2@example.com')

    def test_userIndex_without_authen(self):
        # will redirect to login page
        c = Client()
        response = c.get(reverse('users:index'))
        self.assertEqual(response.status_code, 200)

    def test_userIndex_with_authen(self):
        # status 302 because redirect to register page
        c = Client()
        user = User.objects.get(username='user2')
        c.force_login(user)
        response = c.get(reverse('users:index'))
        self.assertEqual(response.status_code, 302)


    def test_userlogin_login_success(self):
        # status 302 because login success redirect to register page
        c = Client()
        #password = make_password('1234')
        response = c.post(reverse('users:login'),{'username':'user2','password':password})
        self.assertEqual(response.status_code, 302)

    def test_userlogin_login_fail_WrongPass(self):
        # status 302 because login fail redirect to users/index page
        c = Client()
        response = c.post(reverse('users:login'),{'username':'user2','password':'0000'})
        self.assertEqual(response.status_code, 302)

    def test_userlogin_login_fail_WrongUser(self):
        # status 302 because login fail redirect to users/index page
        c = Client()
        response = c.post(reverse('users:login'),{'username':'asdf','password':'1234'})
        self.assertEqual(response.status_code, 302)

    def test_welcome(self):
        # status 200 welcome page
        c = Client()
        response = c.get(reverse('users:wel'))
        self.assertEqual(response.status_code, 200)

    def test_signup(self):
        # status 200 signup page
        c = Client()
        response = c.get(reverse('users:signup'))
        self.assertEqual(response.status_code, 200)

    def test_logout(self):
        # status 302 logout and redireect to login page
        c = Client()
        response = c.get(reverse('users:logout'))
        self.assertEqual(response.status_code, 200)







"""
    def test_index_view_without_authenciation(self):
        c = Client()
        user = User.objects.get(username='user1')
        response = c.get(reverse('users:index'))
        self.assertEqual(response.status_code, 302)

    def test_login_view_unsuccessful(self):
        c = Client()
        user = User.objects.get(username='user1')
        response = c.post(reverse('users:login'), {'username': 'user1', 'password': '1264'})
        self.assertEqual(response.status_code, 200)

    def test_login_view_successful(self):
        c = Client()
        user = User.objects.get(username = "user1")
        response = c.post(reverse('users:login') , {'username': 'user1' , 'password': '1234'})
        self.assertEqual(response.status_code, 302 )

    def test_login_view_index(self):
        c = Client()
        response = c.get(reverse('users:login'))
        self.assertEqual(response.status_code, 200)

    def test_logout_view(self):
        c = Client()
        response = c.get(reverse('users:logout'))
        self.assertEqual(response.status_code, 200)

    def test_studentcourse_without_authenciation(self):
        c = Client()
        response = c.get(reverse('users:studentcourse'))
        self.assertEqual(response.status_code, 302)

    def test_studentcourse_with_authenciation(self):
        c = Client()
        user = User.objects.get(username='user1')
        c.force_login(user)
        response = c.get(reverse('users:studentcourse'))
        self.assertEqual(response.status_code, 200)


   def test_addUser(self):
        # status 302 because login fail redirect to users/index page
        c = Client()
        response = c.post(reverse('users:adduser2'),{'a1':'asdf','a2':'asdf','a3':'asdf','a4':'asdf','a5':'asdf','a6':'asdf','a7':'asdf',})
        self.assertEqual(response.status_code, 302)

"""