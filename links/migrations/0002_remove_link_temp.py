# Generated by Django 4.0 on 2021-12-27 01:34

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('links', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='link',
            name='temp',
        ),
    ]
