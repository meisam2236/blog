from django.contrib import admin
from .models import *

class CustomUserAdmin(admin.ModelAdmin):
    list_display = ['user', 'avatar', 'description']

class ArticleAdmin(admin.ModelAdmin):
    search_fields = ['title', 'content', 'category']
    list_display = ['title', 'category', 'createdDate']

class CategoryAdmin(admin.ModelAdmin):
    list_display = ['title']

admin.site.register(CustomUser, CustomUserAdmin)
admin.site.register(Article, ArticleAdmin)
admin.site.register(Category, CategoryAdmin)
