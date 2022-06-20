# Generated by Django 4.0.5 on 2022-06-20 23:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('backend', '0007_remove_neighborhood_expenses_per_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='neighborhood',
            name='occupancy',
            field=models.DecimalField(decimal_places=4, max_digits=8),
        ),
        migrations.AlterField(
            model_name='neighborhood',
            name='tax_rate',
            field=models.DecimalField(decimal_places=4, max_digits=8),
        ),
        migrations.AlterField(
            model_name='zipcode',
            name='occupancy',
            field=models.DecimalField(decimal_places=4, max_digits=8),
        ),
        migrations.AlterField(
            model_name='zipcode',
            name='tax_rate',
            field=models.DecimalField(decimal_places=4, max_digits=8),
        ),
    ]
