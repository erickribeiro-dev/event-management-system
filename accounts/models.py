from django.contrib.auth.models import AbstractUser
from django.db import models

# Create your models here.
class User(AbstractUser):
    """Represents an User account. This model extends AbstractUser."""
    # Custom fields
    bio = models.CharField(max_length=255, blank=True)

    # Auditing
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.username