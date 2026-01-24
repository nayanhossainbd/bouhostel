from django.db import models
from .models import Rooms

# Create your models here.
class list(models.Model):
    room_id = models.ForeignKey(
        Rooms,
        on_delete=models.CASCADE,
    )