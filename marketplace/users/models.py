from django.contrib.auth.models import AbstractUser, BaseUserManager
from django.db import models


class User(AbstractUser):
    class Role(models.TextChoices):
        BUYER = "BUYER"
        SELLER = "SELLER"

    role = models.CharField(max_length=50, choices=Role.choices, default=Role.BUYER)
    phone = models.CharField(max_length=15, blank=True, null=True)

    def save(self, *args, **kwargs):
        if not self.pk:
            return super().save(*args, **kwargs)


class SellerManager(BaseUserManager):
    def get_queryset(self, *args, **kwargs):
        results = super().get_queryset(*args, **kwargs)
        return results.filter(role=User.Role.SELLER)


class Seller(User):
    objects = SellerManager()
    location = models.TextField(blank=True)

    class Meta:
        verbose_name = "Seller"

    def save(self, *args, **kwargs):
        if not self.pk:
            self.role = User.Role.SELLER
        return super().save(*args, **kwargs)
