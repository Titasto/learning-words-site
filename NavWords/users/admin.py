from django.contrib import admin
from words.models import WordList, Word

admin.site.index_title = 'Manager Room'


class WordInline(admin.TabularInline):
    model = Word
    fields = ['english', 'translation']


@admin.register(WordList)
class MyModelAdmin(admin.ModelAdmin):
    list_display = ['name', 'user']
    list_display_links = ['name']
    list_filter = ['name', 'user']
    save_on_top = True

    inlines = [WordInline,]
