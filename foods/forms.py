from .models import Food
from django import forms
class FoodForm(forms.ModelForm):
    class Meta:
        model = Food
        fields = ["__all__"]

class FoodCategoryForm(forms.ModelForm):
    class Meta:
        model = FoodCategory
        fields = ["__all__"]