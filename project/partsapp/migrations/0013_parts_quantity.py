# Generated by Django 4.2.5 on 2023-11-05 14:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('partsapp', '0012_userprofile'),
    ]

    operations = [
        migrations.AddField(
            model_name='parts',
            name='quantity',
            field=models.PositiveIntegerField(default=0),
        ),
    ]
