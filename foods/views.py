from django.shortcuts import render, get_object_or_404
from .models import Food, FoodCategory

def food_list(request):
    # Fetch categories and include their related food items
    categories = FoodCategory.objects.prefetch_related('foods').all()
    return render(request, 'foods/food_list.html', {'categories': categories})

def food_detail(request, food_id):
    food = get_object_or_404(Food, id=food_id)
    return render(request, 'foods/food_detail.html', {'food': food})