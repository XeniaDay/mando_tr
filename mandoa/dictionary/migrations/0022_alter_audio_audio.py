# Generated by Django 4.1.3 on 2023-01-24 19:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dictionary', '0021_alter_audio_audio'),
    ]

    operations = [
        migrations.AlterField(
            model_name='audio',
            name='audio',
            field=models.FileField(upload_to='media/audio/'),
        ),
    ]
