from django.db import models

# Create your models here.
class Service(models.Model):
    image = models.ImageField(upload_to='images/')
    title = models.CharField(max_length=100)
    home_info = models.CharField(max_length=400)
    service_info_short = models.CharField(max_length=400, default='Shows up in the individual services page')
    service_info_long = models.CharField(max_length=400, default='Shows up in the individual services page')
    cost = models.DecimalField(max_digits=5, decimal_places=2, default=88.00)

    def __str__(self):
        return self.title
