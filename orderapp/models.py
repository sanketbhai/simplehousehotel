from django.db import models

# Create your models here.
class order(models.Model):
    name = models.CharField(max_length=255)
    email = models.CharField(max_length=255)
    address = models.CharField(max_length=255)
    phone = models.CharField(max_length=255)
    products=models.JSONField()
    price=models.CharField(max_length=255)

