# Generated by Django 4.2.5 on 2024-01-30 05:33

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('partsapp', '0028_remove_serviceslot_service_date'),
    ]

    operations = [
        migrations.DeleteModel(
            name='ServiceSlot',
        ),
    ]
