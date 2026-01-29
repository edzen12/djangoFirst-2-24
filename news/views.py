from django.shortcuts import render, get_object_or_404
from news.models import News, Category, AboutPage
from django.db.models import Q


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
    context = {
        'news_all':news_all,
        'category_all':category_all,
    }
    return render(request, 'index.html', context)


def about(request):
    category_all = Category.objects.filter(news__isnull=False).distinct()
    about = AboutPage.objects.latest('-id')
    context = { 
        'category_all':category_all,
        'about':about,
    }
    return render(request, 'about.html', context)


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