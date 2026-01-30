from django.shortcuts import render, get_object_or_404
from .models import Food, FoodCategory

def food_list(request):
    # Fetch categories and include their related food items
    categories = FoodCategory.objects.prefetch_related('foods').all()
    return render(request, 'foods/index.html', {'categories': categories})

def food_detail(request, food_id):
    food = get_object_or_404(Food, id=food_id)
    return render(request, 'foods/details.html', {'food': food})


# View foods for ONE specific category
def food_by_category(request, category_id):
    category = get_object_or_404(FoodCategory, id=category_id)
    foods = category.foods.all() # Get all foods linked to this category
    return render(request, 'foods/category_detail.html', {
        'category': category,
        'foods': foods
    })