from django.urls import path
from apps.news.views import homepage, news_detail, search, category_detail


urlpatterns = [ 
    path('', homepage, name='homepage'),
    path('search/', search, name='search'),
    path('category/<slug:slug>/', category_detail, name='category_detail'),
    path('news/<slug:slug>/', news_detail, name='news_detail'),
]