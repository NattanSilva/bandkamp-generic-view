from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    email = models.EmailField(unique=True,null=False)
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
