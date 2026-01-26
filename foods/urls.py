from django.urls import path
from . import views

urlpatterns = [
    # The name 'food_list' is what you use in {% url 'food_list' %}
    path('foods/', views.food_list, name='food_list'),
    path('food/<int:food_id>/', views.food_detail, name='food_detail'),
]