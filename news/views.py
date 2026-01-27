from django.shortcuts import render, get_object_or_404
from news.models import News, Category, AboutPage
from django.db.models import Q


def search(request):
    pass


def homepage(request):
    news_all = News.objects.all()
    category_all = Category.objects.all()
    context = {
        'news_all':news_all,
        'category_all':category_all,
    }
    return render(request, 'index.html', context)


def about(request):
    category_all = Category.objects.all()
    about = AboutPage.objects.latest('-id')
    context = { 
        'category_all':category_all,
        'about':about,
    }
    return render(request, 'about.html', context)


def news_detail(request, slug):
    news = get_object_or_404(News, slug=slug)
    category_all = Category.objects.all()
    context = {
        'news':news,
        'category_all':category_all,
    }
    return render(request, 'single-page.html',context)