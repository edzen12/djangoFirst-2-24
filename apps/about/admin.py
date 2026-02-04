from django.contrib import admin
from apps.about.models import AboutPage, Employee, SocialLink, Images

@admin.register(AboutPage)
class AboutPageAdmin(admin.ModelAdmin):
    list_display = ['title'] 


class EmployeeInline(admin.TabularInline):
    model = SocialLink
    extra = 1

class ImagesInline(admin.TabularInline):
    model = Images
    extra = 2

@admin.register(Employee)
class EmployeeAdmin(admin.ModelAdmin):
    list_display = ['fullname', 'position']
    inlines = [EmployeeInline, ImagesInline]
    prepopulated_fields = {'slug':['fullname']}

 