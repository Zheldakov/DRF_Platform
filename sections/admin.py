from django.contrib import admin
from sections.models import Section, SectionContent, Tests


@admin.register(Section)
class SectionAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'description')
    list_filter = ('id',)
    ordering = ('id',)


@admin.register(SectionContent)
class ContentAdmin(admin.ModelAdmin):
    list_display = ('id', 'section', 'title',)
    list_filter = ('id', 'section',)
    ordering = ('id', 'section',)


@admin.register(Tests)
class TestsAdmin(admin.ModelAdmin):
    list_display = ('id', 'test_section', 'description', 'question', 'answers')
    list_filter = ('id','test_section',)
    ordering = ('id', 'test_section',)
