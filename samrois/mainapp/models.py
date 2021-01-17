from django.db import models


class Slide(models.Model):
    image = models.ImageField(verbose_name='Изображение (1920х700)', upload_to='img/slides/')

    def __str__(self):
        return str(self.pk)

    class Meta:
        verbose_name = 'Слайд'
        verbose_name_plural = 'Слайды'


class Tour(models.Model):
    name_ru = models.CharField(verbose_name='Название на русском', max_length=200)
    name_en = models.CharField(verbose_name='Название на английском', max_length=200)
    name_ko = models.CharField(verbose_name='Название на корейском', max_length=200)
    img_list = models.ImageField(verbose_name='Мниатюра 370х302', upload_to='img/tours/')
    description_ru = models.TextField(verbose_name='Описание на русском')
    description_en = models.TextField(verbose_name='Описание на английском')
    description_ko = models.TextField(verbose_name='Описание на корейском')
    price = models.BigIntegerField(verbose_name='Цена')

    def __str__(self):
        return self.name_ru

    class Meta:
        verbose_name = 'Тур'
        verbose_name_plural = 'Туры'