from django.db import models


class Contact(models.Model):
    title = models.CharField(max_length=50, verbose_name="Название страницы")
    phone_number1 = models.CharField(max_length=15, verbose_name="Номер телефона 1")
    phone_number2 = models.CharField(
        max_length=15, verbose_name="Номер телефона 2", blank=True, null=True
    )
    phone_number3 = models.CharField(
        max_length=15, verbose_name="Номер телефона 3", blank=True, null=True
    )
    email = models.CharField(max_length=100, verbose_name="Электронная почта")
    map = models.TextField(verbose_name="Ссылка на карту")
    time_to_work = models.CharField(
        max_length=100, verbose_name="Время работы",
        help_text="C 10:00 до 20:00"
    )
    social_whatsapp = models.CharField(
        max_length=100, verbose_name="Ватцап",
        help_text="https://wa.me/996555232323", null=True, blank=True
    )
    social_telegram = models.CharField(
        max_length=100, verbose_name="Telegram",
        help_text="https://t.me/edzen12", null=True, blank=True
    )
    social_instagram = models.CharField(
        max_length=100, verbose_name="Instagram",
        help_text="https://www.instagram.com/edzn.bey/", null=True, blank=True
    )

    def __str__(self):
        return self.title
    
    class Meta:
        verbose_name_plural = 'Контакты'
        verbose_name = 'контакт'


