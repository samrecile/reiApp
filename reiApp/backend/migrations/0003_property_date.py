# Generated by Django 4.0.5 on 2022-06-19 23:36

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('backend', '0002_alter_neighborhood_rent_per_bed'),
    ]

    operations = [
        migrations.AddField(
            model_name='property',
            name='date',
            field=models.DateField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
    ]