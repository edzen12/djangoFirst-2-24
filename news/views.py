from django.shortcuts import render, get_object_or_404
from news.models import News


def homepage(request):
    news_all = News.objects.all()
    context = {
        'news_all':news_all,
    }
    return render(request, 'index.html', context)


def news_detail(request, slug):
    news = get_object_or_404(News, slug=slug)
    context = {
        'news':news,
    }
    return render(request, 'single-page.html',context)