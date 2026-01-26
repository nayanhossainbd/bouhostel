from django.db import models

class FoodCategory(models.Model):
    name = models.CharField(max_length=100)
    
    class Meta:
        verbose_name_plural = "Food Categories"

    def __str__(self):
        return self.name

class Food(models.Model):
    category = models.ForeignKey(FoodCategory, on_delete=models.CASCADE, related_name='foods',null=True)
    name = models.CharField(max_length=200)
    ingredients = models.TextField(help_text="e.g. Chicken, Sun-Dried Tomatoes and Jalapeño")
    image = models.ImageField(upload_to='food_images/')
    medium_price = models.DecimalField(max_digits=6, decimal_places=2)
    large_price = models.DecimalField(max_digits=6, decimal_places=2)
    is_available = models.BooleanField(default=True)

    def __str__(self):
        return self.name