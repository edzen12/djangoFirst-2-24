from django.db import models
from django_ckeditor_5.fields import CKEditor5Field


class AboutPage(models.Model):
    title = models.CharField(max_length=100, verbose_name="Страница")
    desc = CKEditor5Field('Описание о нас', config_name='extends')

    def __str__(self):
        return self.title
    
    class Meta:
        verbose_name_plural = 'О нас'


class Employee(models.Model):
    fullname = models.CharField(max_length=120, verbose_name="ФИО")
    position = models.CharField(max_length=100, verbose_name="Должность")
    exp = models.CharField(max_length=20, verbose_name="Опыт")

    def __str__(self):
        return self.fullname
    
    class Meta:
        verbose_name_plural = 'Сотрудники'
        verbose_name = 'сотрудник'


class SocialLink(models.Model):
    employee = models.ForeignKey(Employee, models.CASCADE)
    title = models.CharField(verbose_name="Название соцсети", max_length=100)
    link = models.CharField(verbose_name="Ссылка на аккаунт", max_length=255)

    def __str__(self):
        return self.title
    
    class Meta:
        verbose_name_plural = 'Соцсети'
        verbose_name = 'соцсеть'
