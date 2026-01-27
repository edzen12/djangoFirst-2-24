from django.db import models
from django_ckeditor_5.fields import CKEditor5Field


class Category(models.Model):
    title =models.CharField(verbose_name="Категория", max_length=50)
    slug = models.SlugField(unique=True)

    def __str__(self):
        return self.title
    
    class Meta:
        verbose_name_plural = 'Категории'


class News(models.Model):
    category = models.ForeignKey(
        Category, on_delete=models.CASCADE, 
        null=True, verbose_name="категория"
    )
    title = models.CharField(max_length=100)
    image = models.ImageField(upload_to='newsMedia/', null=True)
    description = CKEditor5Field('Описание', config_name='extends')
    slug = models.SlugField(unique=True, null=True)

    def __str__(self):
        return self.title
    
    class Meta:
        verbose_name_plural = 'Новости'
    

class AboutPage(models.Model):
    title = models.CharField(max_length=100, verbose_name="Страница")
    desc = CKEditor5Field('Описание о нас', config_name='extends')

    def __str__(self):
        return self.title
    
    class Meta:
        verbose_name_plural = 'О нас'