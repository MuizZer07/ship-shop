from django.db import models
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    is_buyer = models.BooleanField(default=False)
    is_seller = models.BooleanField(default=False)
    phone_number = models.CharField(blank=True, max_length=15)
    rating = models.FloatField(default=0, blank=True)
