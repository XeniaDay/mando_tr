# Generated by Django 4.1.3 on 2023-01-13 19:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dictionary', '0008_delete_dictionary_ts'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='dictionary',
            options={'ordering': ['id'], 'verbose_name': 'Словo', 'verbose_name_plural': 'Слова'},
        ),
        migrations.RemoveField(
            model_name='dictionary',
            name='part_of_speach',
        ),
        migrations.AddField(
            model_name='dictionary',
            name='part_of_speech_en',
            field=models.CharField(default='', max_length=150, verbose_name='Часть речи англ'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='dictionary',
            name='part_of_speech_ru',
            field=models.CharField(default='', max_length=150, verbose_name='Часть речи рус'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='dictionary',
            name='english',
            field=models.CharField(max_length=500, verbose_name='Английский'),
        ),
        migrations.AlterField(
            model_name='dictionary',
            name='russian',
            field=models.CharField(max_length=500, verbose_name='Русский'),
        ),
        migrations.AlterField(
            model_name='dictionary',
            name='written',
            field=models.CharField(max_length=150, verbose_name='Мандор'),
        ),
    ]