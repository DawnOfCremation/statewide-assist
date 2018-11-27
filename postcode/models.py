from django.db import models
from django.db.models import Sum

# Create your models here.
class Postcode(models.Model):
    postcode = models.CharField(max_length=4)
    #postcode = models.IntegerField(Sum('postcode'))
    #suburb = models.CharField(max_length=100, null=True)

    def __str__(self):
        return self.postcode
