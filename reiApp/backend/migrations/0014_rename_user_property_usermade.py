# Generated by Django 4.0.5 on 2022-06-23 01:56

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('backend', '0013_remove_property_active_property_user'),
    ]

    operations = [
        migrations.RenameField(
            model_name='property',
            old_name='user',
            new_name='userMade',
        ),
    ]