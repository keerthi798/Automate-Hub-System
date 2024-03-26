# Generated by Django 5.0.2 on 2024-02-19 17:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('partsapp', '0037_remove_vehicle_images_vehicleimage'),
    ]

    operations = [
        migrations.AlterField(
            model_name='vehicle',
            name='vehicle_application',
            field=models.CharField(choices=[('beverage', 'Beverage'), ('buildingmaterial', 'Building Material'), ('constructionhardware', 'Construction and Hardware'), ('fishery', 'Fishery'), ('fruits_vegetables', 'Fruits and Vegetables'), ('industrial_goods', 'Industrial Goods'), ('lpg_distribution', 'LPG Distribution'), ('school_transport', 'School Transport'), ('tours_travels', 'Tours and Travels')], max_length=20),
        ),
    ]
