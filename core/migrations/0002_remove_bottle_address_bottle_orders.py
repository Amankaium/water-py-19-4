# Generated by Django 4.1 on 2022-08-23 13:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('clients', '0007_order_client'),
        ('core', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='bottle',
            name='address',
        ),
        migrations.AddField(
            model_name='bottle',
            name='orders',
            field=models.ManyToManyField(blank=True, null=True, related_name='bottles', to='clients.order', verbose_name='Заказы'),
        ),
    ]
