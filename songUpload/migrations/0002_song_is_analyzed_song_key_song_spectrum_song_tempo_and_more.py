# Generated by Django 5.1.2 on 2024-11-06 12:58

import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('songUpload', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='song',
            name='is_analyzed',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='song',
            name='key',
            field=models.CharField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='song',
            name='spectrum',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='song',
            name='tempo',
            field=models.FloatField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='song',
            name='upload_date',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
    ]