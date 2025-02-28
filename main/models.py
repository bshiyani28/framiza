from django.contrib.auth.models import AbstractUser
from django.db import models

# Create your models here.

class CustomUser(AbstractUser):
    mobile = models.CharField(max_length=10)

    def __str__(self):
        return self.username


class UserData(models.Model):
    name = models.CharField(max_length=50)
    gender = models.CharField(max_length=10)
    mobile = models.CharField(max_length=15)

