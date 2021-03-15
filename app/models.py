from django.db import models

# Create your models here.
class Crud(models.Model):
    username = models.CharField(max_length=222)
    email = models.EmailField()
    phone = models.CharField(max_length=222)
    password = models.CharField(max_length=222)