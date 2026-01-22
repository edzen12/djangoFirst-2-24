from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from news.views import homepage, news_detail

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', homepage, name='homepage'),
    path('news/<slug:slug>/', news_detail, name='news_detail'),
]+static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)