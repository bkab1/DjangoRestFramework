from django.db import models

# Creating the models here

class Product(models.Model):
    description = models.CharField(max_length=200, blank=False, null=False)
    tag = models.CharField(max_length=100, blank=True, null=True)
    image_url = models.CharField(max_length=200, blank=True, null=True)
