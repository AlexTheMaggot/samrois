# Generated by Django 3.1.4 on 2021-01-30 10:57

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('mainapp', '0010_auto_20210130_1155'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='tour',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='mainapp.tour', verbose_name='Направление'),
        ),
    ]
