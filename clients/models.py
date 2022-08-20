from django.db import models


# Create your models here.
class Client(models.Model):
    name = models.CharField(max_length=255)
    address = models.CharField(max_length=255, null=True, blank=True)
    is_active = models.BooleanField(default=True, verbose_name="Является активным покупателем")
    bottles = models.IntegerField(default=1)
    photo = models.ImageField(
        verbose_name="Фото",
        upload_to='photos',
        null=True,
        blank=True
    )
