from django.db import models

# Create your models here.
class tugas(models.Model):
    username = models.CharField (max_length=250)
    name = models.CharField(max_length=250)