

from django.contrib.auth import views
from students import views
from django.urls import path

urlpatterns = [
    path('students_list/', views.students_list, name='students_list'),
]