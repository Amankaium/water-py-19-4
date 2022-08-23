from django.db import models


class Bottle(models.Model):
    address = models.CharField(max_length=255)
    volume = models.IntegerField(default=10)
    maker = models.CharField(max_length=255)
    description = models.TextField(null=True, blank=True)
    expired = models.BooleanField(default=False)




