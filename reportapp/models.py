from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User

class Article(models.Model):
    name = models.CharField(max_length=100)
    brand = models.CharField(max_length=100, blank=True, null=True)
    category = models.CharField(max_length=100, blank=True, null=True)
    description = models.CharField(max_length=100, blank=True, null=True)
    image = models.ImageField(upload_to='article_images/', blank=True, null=True)
    # lostlocation = models.CharField(max_length=100, blank=True, null=True)
    lostlocation = models.CharField(max_length=255, blank= True, null=True)  # Set a default value
    foundlocation = models.CharField(max_length=255)
    lostdate = models.DateField()
    founddate = models.DateField()
    # create_date = models.DateTimeField(default=timezone.now, null=True,blank=True)
    status = models.CharField(max_length=100, blank=True, null=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE, max_length= 100)

def __str__(self):
    return self.all