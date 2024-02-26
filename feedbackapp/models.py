from django.db import models
from django.contrib.auth.models import User 

# Create your models here.

class Feedback(models.Model):
    feedbackemail= models.CharField(max_length=100 )
    feedbacktext= models.CharField(max_length=500) 
    rate= models.IntegerField(default= 0)
    created_at= models.DateTimeField(auto_now_add=True)
    
    
    
    
    