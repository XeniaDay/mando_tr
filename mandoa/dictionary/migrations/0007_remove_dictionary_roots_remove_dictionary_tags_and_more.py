# Generated by Django 4.1.3 on 2022-12-26 01:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dictionary', '0006_alter_dictionary_options_alter_dictionary_date_load'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='dictionary',
            name='roots',
        ),
        migrations.RemoveField(
            model_name='dictionary',
            name='tags',
        ),
        migrations.AlterField(
            model_name='dictionary',
            name='canon',
            field=models.CharField(blank=True, max_length=150, null=True, verbose_name='Канон'),
        ),
    ]