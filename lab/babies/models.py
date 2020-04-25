from django.db import models

# Create your models here.

class Babie(models.Model):
    firstName = models.CharField(max_length = 200)
    lastName = models.CharField(max_length = 200)