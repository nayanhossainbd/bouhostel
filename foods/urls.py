

from django.contrib.auth import views
from foods import views
from django.urls import path

urlpatterns = [
    path('foods_list/', views.foods_list, name='foods_list'),
]