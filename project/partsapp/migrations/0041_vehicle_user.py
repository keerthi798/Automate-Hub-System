# Generated by Django 5.0.2 on 2024-02-20 09:41

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('partsapp', '0040_vehicle_booking_amount'),
    ]

    operations = [
        migrations.AddField(
            model_name='vehicle',
            name='user',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
