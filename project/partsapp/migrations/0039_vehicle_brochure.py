# Generated by Django 5.0.2 on 2024-02-19 17:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('partsapp', '0038_alter_vehicle_vehicle_application'),
    ]

    operations = [
        migrations.AddField(
            model_name='vehicle',
            name='brochure',
            field=models.FileField(blank=True, null=True, upload_to='vehicle_brochures/'),
        ),
    ]
