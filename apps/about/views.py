from django.shortcuts import render, get_object_or_404
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


def employee_detail(request, slug):
    employee = get_object_or_404(Employee, slug=slug)
    category_all = Category.objects.filter(news__isnull=False).distinct()
    context = {
        'employee':employee,
        'category_all':category_all,
    }
    return render(request, 'single-employee.html',context)