# Generated by Django 4.2.5 on 2023-11-23 15:10

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('partsapp', '0021_delete_servicebooking'),
    ]

    operations = [
        migrations.CreateModel(
            name='ServiceBooking',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('driver_number', models.CharField(max_length=15)),
                ('vehicle_number', models.CharField(max_length=15)),
                ('service_branch', models.CharField(max_length=50)),
                ('vehicle_model', models.CharField(max_length=50)),
                ('service_type', models.CharField(max_length=10)),
                ('service_date', models.DateField()),
                ('email', models.EmailField(default='', max_length=254)),
                ('user', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
