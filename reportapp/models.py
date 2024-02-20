from django.db import models
from django.contrib.auth.models import User 

# Create your models here.
class Article(models.Model):
    name= models.CharField(max_length=100 )
    brand= models.CharField(max_length=100 )
    category= models.CharField(max_length=100, blank=True, null=True )
    description= models.CharField(max_length=100, blank=True, null=True)
    image= models.ImageField(max_length=100, blank=True, null=True)
    lostlocation= models.CharField(max_length=100, blank=True, null=True)
    foundlocation= models.CharField(max_length=100, blank=True, null=True)
    lostdate = models.DateTimeField(auto_now_add=True)
    founddate = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey( User, on_delete = models.CASCADE) 
    
    
