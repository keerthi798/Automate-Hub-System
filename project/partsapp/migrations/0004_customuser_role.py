# Generated by Django 4.2.5 on 2023-11-01 16:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('partsapp', '0003_servicebooking'),
    ]

    operations = [
        migrations.AddField(
            model_name='customuser',
            name='role',
            field=models.CharField(default='', max_length=100),
        ),
    ]
