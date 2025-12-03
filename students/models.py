from django.db import models

# Create your models here.
class Student(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    email = models.EmailField(unique=True)
    enrollment_date = models.DateField()
    father_name = models.CharField(max_length=60)
    mother_name = models.CharField(max_length=60)
    address = models.TextField()
    phone_number = models.CharField(max_length=15)
    

    def __str__(self):
        return f"{self.first_name} {self.last_name}"
