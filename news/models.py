from django.db import models
from django_ckeditor_5.fields import CKEditor5Field

# Create your models here.
class News(models.Model):
    title = models.CharField(max_length=100)
    image = models.ImageField(upload_to='newsMedia/', null=True)
    description = CKEditor5Field('Описание', config_name='extends')
    slug = models.SlugField(unique=True, null=True)

    def __str__(self):
        return self.title
    
    class Meta:
        verbose_name_plural = 'Новости'