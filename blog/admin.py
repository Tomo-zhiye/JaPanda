from django.contrib import admin
from . import models

@admin.register(models.Post)
class AuthorAdmin(admin.ModelAdmin):
    list_display = ('title', 'id', 'status', 'slug', 'author')
    prepopulated_list = {
        'slug': ('title',),
    }

@admin.register(models.Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ('post', 'name', 'email', 'publish_date', 'status')
    list_filter = ('status', 'publish_date')
    search_fields = ('name', 'email', 'comment')

admin.site.register(models.Category)
