from django.db import models
from django.utils import timezone

# Create your models here.

class Attendee(models.Model):
    """
    Description: Registration Form
    """
    full_name = models.CharField(max_length=300)
    company = models.CharField(max_length=300)
    role = models.CharField(max_length=300)
    email = models.EmailField(max_length=100)
    attended = models.BooleanField(default=False)
    reg_key = models.CharField(max_length=300)
    workshop = models.ForeignKey('Workshop', on_delete=models.CASCADE)


class Workshop(models.Model):
    """
    Description: A Workshop and its details
    slug is a human readable key which uniquele identifies a workshop
    """
    slug = models.CharField(max_length=300, unique=True)
    dateandtime = models.DateTimeField(auto_now_add=False)
    title = models.CharField(max_length=300)
    picture_url = models.URLField()
    location = models.CharField(max_length=300)
    