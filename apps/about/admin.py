from django.contrib import admin
from apps.about.models import AboutPage, Employee, SocialLink

@admin.register(AboutPage)
class AboutPageAdmin(admin.ModelAdmin):
    list_display = ['title'] 


class EmployeeInline(admin.TabularInline):
    model = SocialLink
    extra = 1


@admin.register(Employee)
class EmployeeAdmin(admin.ModelAdmin):
    list_display = ['fullname', 'position']
    inlines = [EmployeeInline]

 