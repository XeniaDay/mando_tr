from django.contrib import admin
from .models import Dictionary #, Phrasebook, Audio, Relations


from import_export.admin import ImportExportActionModelAdmin
from import_export import resources
from import_export import fields
from import_export.widgets import ForeignKeyWidget


class DictionaryResource(resources.ModelResource):

    class Meta:
        model = Dictionary

class DictionaryAdmin(ImportExportActionModelAdmin):
    resource_classes = [DictionaryResource]
    list_display = ('id', 'mandoa', 'russian', 'part_of_speech_ru', 'english', 'part_of_speech_en', 'written', 'canon', 'date_load')
    list_display_links = ('mandoa', 'russian', 'part_of_speech_ru', 'english', 'part_of_speech_en')
    search_fields = ('mandoa', 'russian', 'part_of_speech_ru', 'english', 'part_of_speech_en')

admin.site.register(Dictionary, DictionaryAdmin)

'''
class PhrasebookResource(resources.ModelResource):

    class Meta:
        model = Phrasebook

class PhrasebookAdmin(ImportExportActionModelAdmin):
    resource_classes = [PhrasebookResource]
    list_display = ('id', 'mandoa', 'russian', 'comment_rus', 'english', 'comment_eng', 'mandor', 'canon', 'date_load')
    list_display_links = ('mandoa', 'russian', 'comment_rus', 'english', 'comment_eng')
    search_fields = ('mandoa', 'russian', 'comment_rus', 'english', 'comment_eng')

admin.site.register(Phrasebook, PhrasebookAdmin)




class AudioResource(resources.ModelResource):

    class Meta:
        model = Audio

class AudioAdmin(ImportExportActionModelAdmin):
    resource_classes = [AudioResource]
    list_display = ('id', 'title', 'audio')
    search_fields = ('id', 'title')

admin.site.register(Audio, AudioAdmin)



"""
class RelationsResource(resources.ModelResource):

    class Meta:
        model = Relations

class RelationsAdmin(ImportExportActionModelAdmin):
    resource_classes = [RelationsResource]
    list_display = ('id', 'id_1', 'id_2', 'type_rel')
    search_fields = ('type_rel')

admin.site.register(Relations, RelationsAdmin)
"""
class RelationsResource(resources.ModelResource):

    class Meta:
        model = Relations

class RelationsAdmin(ImportExportActionModelAdmin):
    resource_classes = [RelationsResource]
    list_display = ('id', 'id_1', 'id_2', 'type_rel')

admin.site.register(Relations, RelationsAdmin)
'''