# Generated by Django 2.2 on 2021-07-05 01:03

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('tv', '0001_initial'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='User',
            new_name='Show',
        ),
    ]
