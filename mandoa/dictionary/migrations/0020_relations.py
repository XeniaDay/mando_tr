# Generated by Django 4.1.3 on 2023-01-24 00:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dictionary', '0019_alter_audio_audio'),
    ]

    operations = [
        migrations.CreateModel(
            name='Relations',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('id_1', models.CharField(max_length=10, verbose_name='id table1')),
                ('id_2', models.CharField(max_length=10, verbose_name='id table2')),
                ('type_rel', models.CharField(max_length=500, verbose_name='table1 - table2')),
            ],
        ),
    ]
