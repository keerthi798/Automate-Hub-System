# Generated by Django 5.0.2 on 2024-04-07 07:41

import django.db.models.deletion
import django.utils.timezone
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('partsapp', '0065_insurancenew'),
    ]

    operations = [
        migrations.CreateModel(
            name='PaymentRecord',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('amount_paid', models.DecimalField(decimal_places=2, max_digits=10)),
                ('payment_id', models.CharField(max_length=100)),
                ('payment_datetime', models.DateTimeField(default=django.utils.timezone.now)),
                ('insurance', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='partsapp.insurance')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
