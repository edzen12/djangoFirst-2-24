from django.contrib import admin
from apps.news.models import News, Category





@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['title']
    prepopulated_fields = {'slug':['title']}


@admin.register(News)
class NewsAdmin(admin.ModelAdmin):
    list_display = ['title', 'category']
    prepopulated_fields = {'slug':['title']} 