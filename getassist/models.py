from django.db import models

# Create your models here.
class Getassist(models.Model):
    myrego = models.CharField(max_length=10)
    pub_date = models.DateTimeField()
    vehicleMake = models.CharField(max_length=100)
    vehicleModel = models.CharField(max_length=100)
    myName = models.CharField(max_length=100)
    #myPhone = models.IntegerField()
    myLocation = models.CharField(max_length=200)
    mynotes = models.TextField()
