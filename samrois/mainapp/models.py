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
    name_uz = models.CharField(verbose_name='Название на узбекском', max_length=200)
    img_list = models.ImageField(verbose_name='Мниатюра 370х302', upload_to='img/tours/')
    img_detail = models.ImageField(verbose_name='Изображение (870х400)', upload_to='img/tours/')
    description_ru = models.TextField(verbose_name='Описание на русском')
    description_en = models.TextField(verbose_name='Описание на английском')
    description_ko = models.TextField(verbose_name='Описание на корейском')
    description_uz = models.TextField(verbose_name='Описание на узбекском')
    price = models.BigIntegerField(verbose_name='Цена')

    def __str__(self):
        return self.name_ru

    class Meta:
        verbose_name = 'Тур'
        verbose_name_plural = 'Туры'


class Order(models.Model):
    name = models.CharField(verbose_name='Имя', max_length=200, null=True, blank=True)
    phone = models.IntegerField(verbose_name='Номер телефона', null=True, blank=True)
    email = models.CharField(verbose_name='E-mail', max_length=200, null=True, blank=True)
    comment = models.TextField(null=True, blank=True)
    tour = models.ForeignKey(Tour, on_delete=models.SET_NULL, verbose_name='Направление', null=True, blank=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Заявка'
        verbose_name_plural = 'Заявки'
