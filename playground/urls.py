
from django.urls import path
from . import views

urlpatterns = [
    path('', views.home_view, name='home'),
    path('contact.html', views.contact_page, name='contact'),
    path('about.html', views.about_page, name='about'),
    path('rooms.html', views.rooms_page, name='rooms'),
    path('foods.html', views.food_page, name='foods'),

   
]