# Generated by Django 4.2.5 on 2023-11-04 06:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('partsapp', '0005_customuser_address_customuser_phone_number'),
    ]

    operations = [
        migrations.AddField(
            model_name='customuser',
            name='customername',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
    ]
