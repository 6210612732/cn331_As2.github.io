
from django.test import TestCase, Client
from django.urls import reverse
from django.contrib.auth.hashers import make_password
from django.contrib.auth.models import User,auth
from regis.models import Course
from users.models import Student
from django.http import HttpResponseRedirect
from django.shortcuts import redirect, render



class ProjectTestRespond_register(TestCase):
    def setUp(self):
        password = make_password('1234')
        user1 = User.objects.create(username='user1', password=password, email='user1@example.com',is_superuser=True)
        user2 = User.objects.create(username='user2', password=password, email='user2@example.com')
        user3 = User.objects.create(username='user3', password=password, email='user3@example.com')
        course1 = Course.objects.create(c_name='basic python', c_code='cn101', number_of_Applicants=2,
                                        seat=1, status=1,for_year=3, year=2021,)
        course2 = Course.objects.create(c_name='basic java', c_code='cn202', number_of_Applicants=2,
                                        seat=2, status=1,for_year=3, year=2021,)
        course1.student.add(user1)
        course2.student.add(user1)
        course2.student.add(user2)


    def test_register_index(self):
        # redirect to register index
        c = Client()
        response = c.get(reverse('regis:home'))
        self.assertEqual(response.status_code, 200)


    def test_MySubject(self):
        # redirect to mysubject page
        c = Client()
        user = User.objects.get(username='user2')
        c.force_login(user)
        response = c.get(reverse('regis:mysub'))
        self.assertEqual(response.status_code, 200)

    def test_course(self):
        # redirect to course page
        c = Client()
        user = User.objects.get(username='user2')
        c.force_login(user)
        cc = Course.objects.first()
        response = c.get(redirect('/regis/course/1/'))  # 404 not found
        self.assertEqual(response.status_code, 200)