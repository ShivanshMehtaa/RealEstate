from ctypes import addressof
from turtle import title
from django.db import models

# Create your models here.

class Listings(models.Model):
    title = models.CharField(max_length=100)
    price = models.IntegerField()
    num_bedrooms = models.IntegerField()
    num_bathrooms = models.IntegerField()
    square_ft= models.IntegerField()
    address = models.CharField(max_length=1000)
    # image = 

def __str__(self):
    return self.title
    