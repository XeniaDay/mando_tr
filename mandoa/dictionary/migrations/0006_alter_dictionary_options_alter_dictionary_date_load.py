# Generated by Django 4.1.3 on 2022-12-25 02:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dictionary', '0005_alter_dictionary_ts_options_and_more'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='dictionary',
            options={'ordering': ['mandoa'], 'verbose_name': 'Словo', 'verbose_name_plural': 'Слова'},
        ),
        migrations.AlterField(
            model_name='dictionary',
            name='date_load',
            field=models.DateField(verbose_name='Дата загрузки'),
        ),
    ]