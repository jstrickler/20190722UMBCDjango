from django.db import models

class Power(models.Model):
    name = models.CharField(max_length=32, unique=True)
    description = models.CharField(max_length=512)

    def __str__(self):
        return self.name

class City(models.Model):
    name = models.CharField(max_length=32, unique=True)

    def __str__(self):
        return self.name

class Enemy(models.Model):
    name = models.CharField(max_length=32, unique=True)
    powers = models.ManyToManyField(Power)

    def __str__(self):
        return self.name

class Superhero(models.Model):
    name = models.CharField(max_length=32, unique=True)
    real_name = models.CharField(max_length=32)
    secret_identity = models.CharField(max_length=32)
    city = models.ForeignKey(City, on_delete=models.CASCADE)
    powers = models.ManyToManyField(Power)
    enemies = models.ManyToManyField(Enemy)
    favorite_fruit = models.CharField(max_length=32, default="")
    # secret_number = models.FloatField(default=1)

    def __str__(self):
        return self.name


