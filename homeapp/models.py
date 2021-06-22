from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User

# Create your models here.
class Bucket(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE,related_name='bucket',default=1)
    image = models.ImageField(upload_to='photo')
    notes = models.TextField(null=True,blank=True)
    date = models.DateTimeField(default=timezone.now)
    
    
class Article(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE,related_name='article',default=1)
    image =models.ImageField(upload_to='thumbnail')
    heading = models.CharField(max_length=225,default="Article")
    theory = models.TextField(null=True,blank=True)
    date = models.DateTimeField(auto_now_add=True)
    