
#authapp/models.py
from django.contrib.auth.models import AbstractUser
from django.db import models

# Create your models here.

class CustomUser(AbstractUser):
    email = models.EmailField(verbose_name = "Электронная почта", unique=True)
    phone_number = models.CharField(verbose_name = "Номер телефона", max_length=15, blank=True, unique=True)
    
    
    def __str__(self):
        return self.username