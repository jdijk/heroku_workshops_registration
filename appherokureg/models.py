from django.db import models
from django.utils import timezone

# Create your models here.

class RegForm(models.Model):
    """
    Description: Registration Form
    """
    full_name = models.CharField(max_length=300)
    company = models.CharField(max_length=300)
    role = models.CharField(max_length=300)
    email = models.EmailField(max_length=100)
    attended = models.BooleanField(default=False)
    reg_key = models.CharField(max_length=300)


