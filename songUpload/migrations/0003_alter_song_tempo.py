# Generated by Django 5.1.2 on 2024-11-17 08:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('songUpload', '0002_song_is_analyzed_song_key_song_spectrum_song_tempo_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='song',
            name='tempo',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]
