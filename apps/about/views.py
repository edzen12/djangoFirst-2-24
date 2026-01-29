from django.shortcuts import render
from apps.news.models import Category
from apps.about.models import AboutPage, Employee


def about(request):
    category_all = Category.objects.filter(news__isnull=False).distinct()
    about = AboutPage.objects.latest('-id')
    context = { 
        'category_all':category_all,
        'about':about,
    }
    return render(request, 'about.html', context)


def employee(request):
    category_all = Category.objects.filter(news__isnull=False).distinct()
    employee = Employee.objects.prefetch_related('sociallink_set')
    context = { 
        'category_all':category_all,
        'employee':employee,
    }
    return render(request, 'employee.html', context)