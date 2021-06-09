from django.db import models
from django.utils import timezone

# Create your models here.
class Bucket(models.Model):
    image = models.ImageField(upload_to='photo')
    notes = models.TextField(null=True,blank=True)
    date = models.DateTimeField(default=timezone.now)