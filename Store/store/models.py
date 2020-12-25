from django.db import models
from django.contrib.auth.models import AbstractUser
class Store(AbstractUser):
    inn = models.TextField(null=True, blank=True) 
    year_open = models.PositiveIntegerField(null=True, blank=True) 

