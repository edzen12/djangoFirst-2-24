from django.shortcuts import render, get_object_or_404
from apps.news.models import News, Category
from django.db.models import Q
from django.core.paginator import Paginator


def search(request):
    category_all = Category.objects.filter(news__isnull=False).distinct()
    query = request.GET.get('q', '')
    results = []

    if query:
        results = News.objects.filter(
            Q(title__icontains=query) |
            Q(description__icontains=query)
        )
    context = {
        'category_all':category_all,
        'results':results,
        'query':query
    }
    return render(request, 'search.html', context)

def homepage(request):
    news_all = News.objects.all()
    category_all = Category.objects.filter(news__isnull=False).distinct()

    paginator = Paginator(news_all, 3)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    context = {
        'page_obj':page_obj,
        'category_all':category_all,
    }
    return render(request, 'index.html', context)
 

def news_detail(request, slug):
    news = get_object_or_404(News, slug=slug)
    category_all = Category.objects.filter(news__isnull=False).distinct()
    context = {
        'news':news,
        'category_all':category_all,
    }
    return render(request, 'single-page.html',context)


def category_detail(request, slug):
    category = get_object_or_404(Category, slug=slug)
    category_all = Category.objects.filter(news__isnull=False).distinct()
    news_all_category = News.objects.filter(category=category)
    context = {
        'category_all':category_all,
        'category':category,
        'news_all_category':news_all_category,
    }
    return render(request, 'category.html', context)