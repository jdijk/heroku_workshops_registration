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

    def __str__(self):
        return str(self.email)


class Workshop(models.Model):
    """
    Description: A Workshop and its details
    slug is a human readable key which uniquele identifies a workshop
    """
    slug = models.CharField(max_length=300, unique=True)
    dateandtime = models.DateTimeField(auto_now_add=False)
    title = models.CharField(max_length=300)
    picture_url = models.URLField(blank=True)
    location = models.CharField(max_length=300)
    long_description = models.TextField()
    active = models.BooleanField(default=True)

    def __str__(self):
        return str(self.slug)


class CampaignMember(models.Model):
    # this meta option will ensure migrate doesn't create tables for this mode
    # as it'll already be availabe for us via Heroku Connect.
    class Meta:
        managed = False
        db_table = '"salesforce"."campaignmember"'

    campaignid = models.CharField(max_length=300)
    name = models.CharField(max_length=300)
    sfid = models.CharField(max_length=300)
    status = models.CharField(max_length=300)
    email = models.CharField(max_length=300)


class Campaign(models.Model):
    class Meta:
        managed = False
        db_table = '"salesforce"."campaign"'

    name = models.CharField(max_length=300)
    sfid = models.CharField(max_length=300)
