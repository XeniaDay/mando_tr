# Generated by Django 4.1.3 on 2023-01-21 22:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dictionary', '0010_phrasebook'),
    ]

    operations = [
        migrations.AlterField(
            model_name='phrasebook',
            name='canon',
            field=models.CharField(blank=True, max_length=10, null=True, verbose_name='Канон'),
        ),
        migrations.AlterField(
            model_name='phrasebook',
            name='comment_eng',
            field=models.CharField(blank=True, max_length=500, verbose_name='Комментарий англ'),
        ),
        migrations.AlterField(
            model_name='phrasebook',
            name='comment_rus',
            field=models.CharField(blank=True, max_length=500, verbose_name='Комментарий англ'),
        ),
    ]