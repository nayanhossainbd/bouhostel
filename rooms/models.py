from django.db import models
class Room(models.Model):
    room_number = models.CharField(max_length=10, unique=True)
    capacity = models.IntegerField()
    total_beds = models.IntegerField()
    rate_per_bed = models.DecimalField(max_digits=8, decimal_places=2)
    is_available = models.BooleanField(default=True)

    def __str__(self):
        return f"Room {self.room_number} - Capacity: {self.capacity} - Available: {self.is_available}"

# Create your models here.
