from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    ROLE_CHOICES = (
        ('ADMIN', 'Admin'),
        ('ANALYST', 'Analyst'),
    )

    role = models.CharField(
        max_length=10,
        choices=ROLE_CHOICES,
        default='ANALYST'
    )

    def __str__(self):
        return f"{self.username} ({self.role})"
