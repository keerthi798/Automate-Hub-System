# Generated by Django 5.0.2 on 2024-04-07 11:22

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('partsapp', '0066_paymentrecord'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='paymentrecord',
            name='payment_id',
        ),
    ]
