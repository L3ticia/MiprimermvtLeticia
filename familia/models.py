from django.db import models

# Create your models here.
import uuid

# Create your models here.
class familia (models.Model):
    id = models.CharField(default= uuid.uuid4(),primary_key=True, max_length=100)
    nombre = models.CharField(max_length=50)
    edad = models.IntegerField()
    cumpleaños = models.DateField()