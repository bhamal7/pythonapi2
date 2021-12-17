from django.db import models

# Create your models here.

class Hero(models.Model):
    name = models.CharField(max_length= 15)
    age = models.IntegerField()
    gender = models.CharField(max_length= 15)

    def __str__(self):
        return self.name
