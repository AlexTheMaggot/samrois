# Generated by Django 3.1.4 on 2021-01-30 06:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mainapp', '0008_tour_img_detail'),
    ]

    operations = [
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200, verbose_name='Имя')),
                ('phone', models.IntegerField(verbose_name='Номер телефона')),
                ('email', models.CharField(max_length=200, verbose_name='E-mail')),
                ('comment', models.TextField()),
            ],
            options={
                'verbose_name': 'Заявка',
                'verbose_name_plural': 'Заявки',
            },
        ),
    ]
