from django.contrib import admin
from django.urls import path,include


from . import views

app_name = "users"
urlpatterns = [
    path('',views.index , name="index"),
    path('login',views.login_view , name="login"),
    path('logout',views.logout_view , name="logout"),
    path('wel',views.wel , name="wel"),
    path('signup',views.signup , name="signup"),
  #  path('adduser2',views.adduser, name="adduser2"),
]
