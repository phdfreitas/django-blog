from typing import Dict
from django.contrib import admin
from . models import Post


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ('titulo', 'subtitulo', 'autor', 'publicacao', 'status')
    list_filter = ['titulo', 'subtitulo', 'autor']
    date_hierarchy = 'publicacao'
    search_fields = ['titulo', 'subtitulo', 'autor']
    prepopulated_fields = {'slug':['titulo', 'subtitulo'[:20]]}
    