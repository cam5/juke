# Generated by Django 2.0.7 on 2018-07-24 20:55

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('playlists', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Release',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('date', models.DateTimeField(blank=True)),
                ('country', models.CharField(max_length=100)),
                ('label', models.CharField(max_length=100)),
                ('catalogue_number', models.CharField(max_length=100)),
                ('barcode', models.CharField(max_length=100)),
                ('status', models.CharField(max_length=14, verbose_name=[('Bootleg', 'Bootleg'), ('Official', 'Official'), ('Promotional', 'Promotional'), ('Pseudo-Release', 'Pseudo-Release')])),
                ('mbid', models.CharField(blank=True, max_length=100)),
            ],
        ),
        migrations.AlterField(
            model_name='artist',
            name='gender',
            field=models.CharField(default='None', max_length=6, verbose_name=[('Female', 'Female'), ('Male', 'Male'), ('None', 'None')]),
        ),
        migrations.AlterField(
            model_name='artist',
            name='type',
            field=models.CharField(max_length=100, verbose_name=[('Character', 'Character'), ('Choir', 'Choir'), ('Group', 'Group'), ('Orchestra', 'Orchestra'), ('Other', 'Other'), ('Person', 'Person')]),
        ),
        migrations.AddField(
            model_name='release',
            name='artist',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='playlists.Artist'),
        ),
    ]