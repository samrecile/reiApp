# Generated by Django 4.0.5 on 2022-06-20 23:12

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('backend', '0009_remove_neighborhood_zip_code'),
    ]

    operations = [
        migrations.RenameField(
            model_name='property',
            old_name='zipCode',
            new_name='zipcode',
        ),
    ]
