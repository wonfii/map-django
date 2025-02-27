from django.db import models

# Create your models here.
class Place(models.Model):
    name = models.CharField(max_length=250)
    latitude = models.FloatField()
    longitude = models.FloatField()
    location = models.CharField(max_length=100, default='not indicated', null=True)
    
    def __str__(self):
        return self.name