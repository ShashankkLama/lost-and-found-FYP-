from django.db import models
from django.contrib.auth.models import User 

# Create your models here.
class Article(models.Model):
    name= models.CharField(max_length=100 )
    brand= models.CharField(max_length=100 )
    category= models.CharField(max_length=100 )
    description= models.CharField(max_length=100 )
    image= models.ImageField(max_length=100 )
    lostlocation= models.CharField(max_length=100 )
    foundlocation= models.CharField(max_length=100 )
    lostdate= models.DateTimeField(max_length=100 )
    founddate= models.DateTimeField(max_length=100 )
    create_date= models.DateTimeField()
    user = models.ForeignKey( User, on_delete = models.CASCADE, blank=True, null=True) 
    
    
