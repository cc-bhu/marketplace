from django.db import models


# Create your models here.
class seller(models.Model):
    name = models.CharField(max_length=50)
    phone = models.CharField(max_length=15)
    email = models.EmailField(unique=True)
    location = models.TextField(blank=True)
