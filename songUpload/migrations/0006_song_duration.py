# Generated by Django 5.1.2 on 2024-11-18 15:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('songUpload', '0005_alter_song_danceability'),
    ]

    operations = [
        migrations.AddField(
            model_name='song',
            name='duration',
            field=models.CharField(blank=True, null=True),
        ),
    ]