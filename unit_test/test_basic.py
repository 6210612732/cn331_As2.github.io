
from django.test import TestCase, Client
from django.urls import reverse
from django.contrib.auth.hashers import make_password
from django.contrib.auth.models import User,auth
from regis.models import Course
from users.models import Student
from django.http import HttpResponseRedirect
from django.shortcuts import redirect, render

