from django.db import models


class RoomCategory(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(blank=True)

    def __str__(self):
        return self.name

class Room(models.Model):
    name = models.CharField(max_length=255)
    room_number = models.CharField(max_length=10, unique=True)
    capacity = models.IntegerField()
    total_beds = models.IntegerField()
    rate_per_bed = models.DecimalField(max_digits=8, decimal_places=2)
    is_available = models.BooleanField(default=True)
    short_desc=  models.TextField( null=True)
    description = models.TextField(blank=True, null=True)
    price = models.DecimalField(max_digits=7, decimal_places=2, blank=True, null=True)
    # Images will be stored in media/products/ directory
    image = models.ImageField(upload_to='rooms/', blank=True, null=True)

    def __str__(self):
        return f" Name: {self.name} - Price: {self.price} Room {self.room_number} - Capacity: {self.capacity} - Available: {self.is_available} -{self.name}"

    
    # Optional: Add a property to get the image URL more cleanly in templates
    @property
    def imageURL(self):
        try:
            url = self.image.url
        except:
            url = '' # Use a placeholder image path here if needed
        return url