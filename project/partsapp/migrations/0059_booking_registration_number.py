# Generated by Django 5.0.2 on 2024-04-02 10:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('partsapp', '0058_confirmedvehicle'),
    ]

    operations = [
        migrations.AddField(
            model_name='booking',
            name='registration_number',
            field=models.CharField(blank=True, max_length=20, null=True),
        ),
    ]
