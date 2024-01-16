from django.db import models

# Create your models here.
class Items(models.Model):
    name= models.CharField(max_length=100 )
    brand= models.CharField(max_length=100 )
    category= models.CharField(max_length=100 )
    description= models.CharField(max_length=100 )
    image= models.ImageField(max_length=100 )
    lostlocation= models.CharField(max_length=100 )
    foundlocation= models.CharField(max_length=100 )
    lostdate= models.DateTimeField(max_length=100 )
    founddate= models.DateTimeField(max_length=100 )
    