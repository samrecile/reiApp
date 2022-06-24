# Generated by Django 4.0.5 on 2022-06-23 22:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('backend', '0016_property_cap_rate'),
    ]

    operations = [
        migrations.AlterField(
            model_name='property',
            name='cap_rate',
            field=models.DecimalField(blank=True, decimal_places=4, max_digits=6, null=True),
        ),
    ]