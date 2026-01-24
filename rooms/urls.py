


from django.contrib.auth import views
from rooms import views
from django.urls import path

urlpatterns = [
    path('rooms_list/', views.rooms_list, name='rooms_list')
]