from django.db import models


# Create your models here.

class Restaurant(models.Model):
    name = models.CharField(max_length=200)
    address = models.CharField(max_length=200)
    phone_number = models.CharField(max_length=20)
    website = models.CharField(max_length=200)
    description = models.CharField(max_length=200)
    rating = models.IntegerField(default=0)
    service_speed = models.IntegerField(default=0)
    price = models.IntegerField(default=0)
    menu = models.CharField(max_length=200)

    def __str__(self):
        return self.name
