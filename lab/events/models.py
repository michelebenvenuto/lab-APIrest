from django.db import models
from babies.models import Babie

# Create your models here.

class Event(models.Model):
    eventName = models.CharField(max_length = 50)
    eventType = models.CharField(max_length = 50)
    description = models.CharField(max_length = 200)
    eventDate = models.DateField(auto_now_add= True)
    eventsToBaby= models.ManyToManyField(Babie)