# Generated by Django 4.2.5 on 2023-11-04 05:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('partsapp', '0004_customuser_role'),
    ]

    operations = [
        migrations.AddField(
            model_name='customuser',
            name='address',
            field=models.TextField(blank=True),
        ),
        migrations.AddField(
            model_name='customuser',
            name='phone_number',
            field=models.CharField(blank=True, max_length=15, null=True),
        ),
    ]
