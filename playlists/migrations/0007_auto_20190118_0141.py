# Generated by Django 2.0.7 on 2019-01-18 01:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('playlists', '0006_auto_20190118_0135'),
    ]

    operations = [
        migrations.AlterField(
            model_name='release',
            name='barcode',
            field=models.CharField(max_length=100, null=True),
        ),
    ]