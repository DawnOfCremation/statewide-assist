from django.db import models

# Create your models here.
class Faq(models.Model):
    question = models.CharField(max_length=100, default='add question here')
    answer = models.CharField(max_length=200, default='add answer here')
    heading_number = models.CharField(max_length=50, default='eg - headingOne')
    collapse_number = models.CharField(max_length=50, default='eg - collapseOne')

    def __str__(self):
        return self.question
