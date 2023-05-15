from django.core.validators import FileExtensionValidator
from django.db import models



class Dictionary (models.Model):
    mandoa = models.CharField(verbose_name="Мандо'а", max_length=150)
    pronunciation = models.CharField(verbose_name="Произношение", max_length=150)
    english = models.CharField(verbose_name="Английский", max_length=500)
    russian = models.CharField(verbose_name="Русский", max_length=500)
    part_of_speech_en = models.CharField(verbose_name="Часть речи англ", max_length=150)
    part_of_speech_ru = models.CharField(verbose_name="Часть речи рус", max_length=150)
    written = models.CharField(verbose_name="Мандор", max_length=150)
    canon = models.CharField(verbose_name="Канон", max_length=150, null=True, blank=True)
#    roots = models.CharField (verbose_name="ID корней", max_length=150)
#    tags = models.CharField (verbose_name="Тэги", max_length=1500)
    date_load = models.DateField(verbose_name="Дата загрузки")

    def __str__(self):
        return self.mandoa + ' - ' + self.russian

    class Meta:
        verbose_name='Словo'
        verbose_name_plural='Слова'
        ordering = ['id']


#class GrammarRules (models.Model):


'''
class Phrasebook (models.Model):
    mandoa = models.CharField (verbose_name="Мандо'а", max_length=500)
    mandor = models.CharField (verbose_name="Мандор", max_length=500)
    english = models.CharField (verbose_name="Английский", max_length=500)
    comment_eng = models.CharField (verbose_name="Комментарий англ", max_length=500, null=True, blank=True)
    russian = models.CharField (verbose_name="Русский", max_length=500)
    comment_rus = models.CharField (verbose_name="Комментарий рус", max_length=500, null=True, blank=True)
    canon = models.CharField (verbose_name="Канон", max_length=10, null=True, blank=True)
    date_load = models.DateField (verbose_name="Дата загрузки")

    def __str__(self):
        return self.mandoa + ' - ' + self.russian

    class Meta:
        verbose_name='Фраза'
        verbose_name_plural='Фразы'
        ordering = ['id']




class Audio (models.Model):
    title = models.CharField(verbose_name="Мандо'а", max_length=500)
    audio = models.FileField(upload_to='audio/')

    def __str__(self):
        return self.title



class Relations (models.Model):
    id_1 = models.CharField(verbose_name="id table1", max_length=10)
    id_2 = models.CharField(verbose_name="id table2", max_length=10)
    type_rel = models.CharField(verbose_name="table1 - table2", max_length=500)

    def __str__(self):
        return self.type_rel
'''