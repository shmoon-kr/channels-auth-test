from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.


class CustomUser(AbstractUser):

    email = models.EmailField(unique=True, blank=False, max_length=254, verbose_name="email address")

    USERNAME_FIELD = "email"   # e.g: "username", "email"
    EMAIL_FIELD = "email"         # e.g: "email", "primary_email"
    REQUIRED_FIELDS = []
