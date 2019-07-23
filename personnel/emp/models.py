from django.db import models

# Create your models here.

class City(models.Model):
    name = models.CharField(max_length=64)

class Employee(models.Model):
    first_name = models.CharField(max_length=32)
    last_name = models.CharField(max_length=32)
    dob = models.DateField()
    city = models.ForeignKey(City, on_delete=models.CASCADE)


