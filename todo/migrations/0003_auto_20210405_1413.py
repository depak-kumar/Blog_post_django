# Generated by Django 3.0 on 2021-04-05 11:13

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('todo', '0002_auto_20210405_1406'),
    ]

    operations = [
        migrations.RenameField(
            model_name='todo',
            old_name='create',
            new_name='created',
        ),
    ]
