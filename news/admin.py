from django.contrib import admin
from news.models import News
# Register your models here.

class NewsAdmin(admin.ModelAdmin):
    list_display = ['title']
    prepopulated_fields = {'slug':['title']}

admin.site.register(News, NewsAdmin)