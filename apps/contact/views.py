from django.shortcuts import render
from apps.contact.models import Contact
from apps.news.models import Category


def contact(request):
    contacts = Contact.objects.latest('-id')
    category_all = Category.objects.filter(news__isnull=False).distinct()
    context = {
        'contacts':contacts,
        'category_all':category_all,
    }
    return render(request, 'contact.html', context)