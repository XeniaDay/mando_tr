# Generated by Django 4.1.3 on 2023-01-23 19:42

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('dictionary', '0015_audio'),
    ]

    operations = [
        migrations.RenameField(
            model_name='audio',
            old_name='mandoa',
            new_name='title',
        ),
    ]
