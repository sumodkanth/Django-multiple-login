from django.db import models
from django.contrib.auth.models import AbstractUser


# Create your models here.
class Customuser(AbstractUser):
    phone = models.CharField(max_length=20)
    is_admin = models.BooleanField(default=False)
    is_student = models.BooleanField(default=False)
    is_teacher = models.BooleanField(default=False)
