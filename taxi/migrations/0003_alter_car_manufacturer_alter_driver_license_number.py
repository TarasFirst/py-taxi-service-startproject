# Generated by Django 5.0.6 on 2024-07-07 12:01

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("taxi", "0002_alter_car_manufacturer"),
    ]

    operations = [
        migrations.AlterField(
            model_name="car",
            name="manufacturer",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE, to="taxi.manufacturer"
            ),
        ),
        migrations.AlterField(
            model_name="driver",
            name="license_number",
            field=models.CharField(max_length=100, unique=True),
        ),
    ]
