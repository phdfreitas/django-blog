from typing import Dict
from django.contrib import admin
from . models import Post


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ('titulo', 'autor', 'publicacao', 'status')
    list_filter = ['titulo', 'autor']
    date_hierarchy = 'publicacao'
    search_fields = ['titulo']
    prepopulated_fields = {'slug':('status', 'titulo')}
    