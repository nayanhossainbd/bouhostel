from django.urls import path
from . import views

urlpatterns = [
    path('', views.home_view,),
    path('contact', views.contact_page),
    path('rooms', views.rooms_page, name='room_list'),
    path('room/<int:room_id>/', views.room_detail, name='room_detail'),
    path('foods', views.food_page, name='food_list'),
    path('food/<int:food_id>/', views.food_detail, name='food_detail'),
    path('buy/<int:room_id>/', views.buy_room, name='buy_room'),
    path('summary/', views.booking_summary, name='booking_summary'),
    path('about', views.about_page, name='about'), # Added a trailing slash
    path('contact/', views.contact_page, name='contact'),
]