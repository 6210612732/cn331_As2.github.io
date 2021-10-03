from django.urls import path,include

from . import views


app_name = "regis"
urlpatterns = [
    path('',views.index , name="home"),
    path('regis_<int:course_id>',views.regis , name="regis"),
    path('cancel_<int:course_id>_<int:ffrom>',views.cancel , name="cancel"),
    path('mysub',views.mysub , name="mysub"),
    path('course/<course_id>/',views.course , name="course"),
]
