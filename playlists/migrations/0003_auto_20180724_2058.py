# Generated by Django 2.0.7 on 2018-07-24 20:58

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('playlists', '0002_auto_20180724_2055'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='artist',
            name='ipi',
        ),
        migrations.RemoveField(
            model_name='artist',
            name='isni',
        ),
    ]
