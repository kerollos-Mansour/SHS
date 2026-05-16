from django.db import models
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    ROLE_ADMIN = 'ADMIN'
    ROLE_SALES = 'SALES'

    ROLE_CHOICES = (
        (ROLE_ADMIN, 'Admin'),
        (ROLE_SALES, 'Sales User'),
    )

    role = models.CharField(max_length=20, choices=ROLE_CHOICES, default=ROLE_SALES)

    def is_admin(self):
        return self.role == self.ROLE_ADMIN or self.is_superuser

    def is_sales(self):
        return self.role == self.ROLE_SALES
