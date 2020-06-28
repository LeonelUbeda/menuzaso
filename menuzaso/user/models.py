from django.db import models
from django.contrib.auth.models import AbstractUser
# Create your models here.
from restaurant.models import Restaurant

class User(AbstractUser):
    restaurant = models.ForeignKey(Restaurant, on_delete=models.CASCADE, blank=False, null=True)

