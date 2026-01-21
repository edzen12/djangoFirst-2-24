from django.db import models

# Create your models here.
class News(models.Model):
    title = models.CharField(max_length=100)
    image = models.ImageField(upload_to='newsMedia/', null=True)
    description = models.TextField()

    def __str__(self):
        return self.title
    
    class Meta:
        verbose_name_plural = 'Новости'