from django.urls import path
from . import views

urlpatterns = [
    path('', views.home_view,),
    path('contact', views.contact_page),
    path('rooms', views.rooms_page, name='room_list'),
    path('room/<int:room_id>/', views.room_detail, name='room_detail'),
    path('buy-room/<int:room_id>/', views.buy_room, name='buy_room'),
    path('foods', views.food_page, name='food_list'),
    path('food/<int:food_id>/', views.food_detail, name='food_detail'),
    path('order-food/<int:food_id>/', views.order_food, name='order_food'),
    path('summary/', views.booking_summary, name='booking_summary'),
    path('about', views.about_page, name='about'), # Added a trailing slash
    path('contact/', views.contact_page, name='contact'),
    path('checkout-food/', views.checkout_food, name='checkout_food'),
    path('checkout-room/', views.checkout_room, name='checkout_room'),
]