from django.db import models
from clients.models import Order


class Bottle(models.Model):
    volume = models.IntegerField(default=10)
    maker = models.CharField(max_length=255)
    description = models.TextField(null=True, blank=True)
    expired = models.BooleanField(default=False)

    orders = models.ManyToManyField(
        to=Order,
        null=True, blank=True,
        verbose_name="Заказы",
        related_name="bottles"
    )





