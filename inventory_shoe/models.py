from django.db import models


# model definition

class Inventory_shoe(models.Model):
    name = models.CharField(max_length=70, blank=False, default='')
    description = models.CharField(max_length=200, blank=False, default='')
    available = models.BooleanField(default=False)
