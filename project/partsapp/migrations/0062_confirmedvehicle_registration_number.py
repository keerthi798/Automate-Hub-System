# Generated by Django 5.0.2 on 2024-04-05 18:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('partsapp', '0061_vehicleregistration'),
    ]

    operations = [
        migrations.AddField(
            model_name='confirmedvehicle',
            name='registration_number',
            field=models.CharField(blank=True, max_length=20, null=True),
        ),
    ]
